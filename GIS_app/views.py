from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    return render(request, 'GIS_app/index.html')

def elevation(request):
    return render(request, 'GIS_app/elevation.html')

def home(request):
    return render(request, 'GIS_app/home.html')
