from django.urls import path
from rcb.views import *

app_name = 'name3'

urlpatterns = [
    path('virat/',virat,name='virat'),
    path('virat1/',virat1,name='virat1'),
]
