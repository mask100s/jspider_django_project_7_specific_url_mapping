from django.urls import path
from mi.views import *

app_name = 'name2'

urlpatterns = [
    path('rohit/',rohit,name='rohit'),
    path('rohit1/',rohit1,name='rohit1'),
]
