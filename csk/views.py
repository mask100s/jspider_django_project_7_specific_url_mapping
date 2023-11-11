from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def msd(request):
  return render(request,'msd.html')

def msd1(request):
  return HttpResponse('<center><h1>MSD plays for csk</h1></center>')

