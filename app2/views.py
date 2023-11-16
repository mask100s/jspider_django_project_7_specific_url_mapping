from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def newziland(request):
  return render(request,'newziland1.html')

def newziland1(request):
  return HttpResponse('<h1>this is a http string response for nz</h1>')
