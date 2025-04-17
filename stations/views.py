from django.shortcuts import render
from .models import Station

# Create your views here.

def home(request):
    return render(request, "home.html")

def map(request):
    stations = Station.objects.all()
    return render(request, "map.html", {"stations": stations})