from django.urls import path
from .views import *

app_name = 'task1'

urlpatterns = [
    path('task1', task, name='task'),
]
