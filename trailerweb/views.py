from django.shortcuts import render
from .models import Mainiki

def home(request):

    return render(request, 'index.html', {})


def detail(request):
    return render(request, 'detail.html', {})