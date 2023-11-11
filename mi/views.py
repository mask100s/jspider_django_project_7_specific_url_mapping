from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rohit(request):
  return render(request,'rohit.html')

def rohit1(request):
  return HttpResponse('<center><h1>Rohit plays for mi</h1></center>')

