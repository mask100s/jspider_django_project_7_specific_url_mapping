from app1.views import *
from django.urls import path

app_name="anything1"


urlpatterns=[
  path('india/', india ,name='india'),
  path('india1/', india1 ,name='india1'),
]