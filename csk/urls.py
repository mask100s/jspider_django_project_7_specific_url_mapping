from django.urls import path
from csk.views import *

app_name = 'name1'

urlpatterns = [
    path('msd/',msd,name='msd'),
    path('msd1/',msd1,name='msd1'),
]
