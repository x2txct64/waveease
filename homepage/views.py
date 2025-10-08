from django.shortcuts import render
from . import views
from django.urls import path

# Create your views here.
def home(request):
    return render(request, "homepage/home.html")

def about(request):
    return render(request, "homepage/about.html")

def assist(request):
    return render(request, "homepage/assist.html")