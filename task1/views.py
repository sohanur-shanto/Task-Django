from django.shortcuts import render
from .models import *
from itertools import chain
from operator import attrgetter
from django.http import HttpResponse


def task(request):
    footballdata = Football.objects.all()
    cricketdata = Cricket.objects.all()
    football = list(footballdata)
    cricket = list(cricketdata)
    result = list(football) + list(cricket)
    result_data = footballdata.union(cricketdata, all=True)
    
    merged_list = sorted(   
        chain(footballdata, cricketdata),
        key=attrgetter('date_created'))

    return render(request, 'task1/task1.html', {'merged_list' : merged_list, 'footballdata' : footballdata, 'cricketdata' : cricketdata, 'result' : result, 'result_data' : result_data})
