from app2.views import *
from django.urls import path

app_name="anything2"


urlpatterns=[
  path('newziland/',newziland,name='newziland'),
  path('newziland1/',newziland1,name='newziland1'),
]