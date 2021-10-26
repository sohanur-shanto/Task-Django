from django.shortcuts import render
from django.utils.translation import activate
from .forms import CsvModelForm
from .models import Csv, Data
import csv
from .utils import get_plot, get_boxplot, get_histogram
import numpy as np
import matplotlib.pyplot as plt
from django.http import HttpResponse, response
from django.core.paginator import EmptyPage, Paginator
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from django.db import transaction


@transaction.atomic
def upload_file_view(request):
    start_time = datetime.now()
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    date = row[0]
                    appl_open = row[1]
                    appl_high = row[2]
                    appl_low = row[3]
                    appl_close = row[4]
                    appl_volume = row[5]
                    appl_adjusted = row[6]
                    dn = row[7]
                    mavg = row[8]
                    up = row[9]
                    direction = row[10]

                    Data.objects.bulk_create([
                        Data (
                            date = date, appl_open = appl_open, appl_high = appl_high, appl_low = appl_low,
                            appl_close = appl_close, appl_volume = appl_volume, appl_adjusted = appl_adjusted,
                            dn = dn, mavg = mavg, up = up, direction = direction 
                            )                   
                    ])
                   
            obj.activated = True
            obj.save()
            end_time = datetime.now()
            print('Duration: {}'.format(end_time - start_time))

    return render(request, 'core/task.html', {'form' : form})



def get_data(request):
    dataset = Data.objects.all()
    qs = Data.objects.get_queryset().order_by('id')
    x = [x.appl_low for x in dataset]
    y = [y.appl_high for y in dataset]
    z = [z.appl_open for z in dataset]
    w = [w.appl_close for w in dataset]
    v = [v.appl_volume for v in dataset]
    area = 14
    colors = np.random.rand(len(x))
    chart = get_plot(z, w, area, colors)
    data_1 = np.random.normal(x)
    data_2 = np.random.normal(y)
    data_3 = np.random.normal(z)
    data_4 = np.random.normal(w)
    data_5 = np.random.normal(v)
    data = [data_1, data_2, data_3, data_4]
    chart2 = get_boxplot(data)
    chart3 = get_histogram(data_5)
    p = Paginator(qs, 5)
    page_num = request.GET.get('page', 1)

    try :
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, 'core/table.html', {'dataset': dataset, 'qs': page, 'chart': chart, 'chart2': chart2, 'chart3': chart3})


def d_csv(request):
    dataset = Data.objects.all()
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=data.csv'
    writer = csv.writer(response)

    writer.writerow(['Date', 'aapl_open', 'appl_high', 'appl_low', 'appl_close', 'appl_volume', 'appl_adjusted', 'dn', 'mavg', 'up', 'direction'])

    for data in dataset:
        writer.writerow([data.date, data.appl_open, data.appl_high, data.appl_low, data.appl_close, data.appl_volume, data.appl_adjusted, data.dn, data.mavg, data.up, data.direction ])
    return response

