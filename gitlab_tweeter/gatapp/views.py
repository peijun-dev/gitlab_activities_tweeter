from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'gatapp/index.html')

def temp(request):
    return render(request, 'gatapp/temp.html')