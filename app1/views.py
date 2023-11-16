from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def india(request):
  return HttpResponse('<h1>this is a http string response for ind</h1>')

def india1(request):
  return render(request,'india1.html')