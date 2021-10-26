import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph



def get_plot(z, w, area, colors):
    plt.figure(figsize=(10,5))
    plt.title('Scatter Plot')
    plt.xticks(rotation = 45)
    plt.xlabel('APPL Open')
    plt.ylabel('APPL Close')
    plt.scatter(z, w, s=area, c=colors, alpha=0.5)
    graph = get_graph()
    return graph



def get_boxplot(data):
    plt.figure(figsize=(10,5))
    plt.title('Box Plot for APPL Low, APPL High, APPL Open, AAPL Close')
    plt.boxplot(data)
    graph = get_graph()
    return graph


def get_histogram(data_5):
    plt.figure(figsize=(10,5))
    plt.title('Histogram')
    plt.xlabel('Apple Volume')
    colors = ['green']
  
    plt.hist(data_5, density = True, 
         histtype ='bar',
         color = colors,
         label = colors)
    graph = get_graph()
    return graph