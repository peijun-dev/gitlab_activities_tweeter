from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'gatapp/index.html')

def temp(request):
    return render(request, 'gatapp/temp.html')

@login_required
def private(request):
    return render(request, 'gatapp/gitlab.html')