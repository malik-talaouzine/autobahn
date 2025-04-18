from django.shortcuts import render
from .models import Station, ParkingLorry

# Create your views here.

def home(request):
    return render(request, "home.html")

def map(request):
    stations = Station.objects.all()
    lorries = ParkingLorry.objects.all()
    return render(request, "map.html", {"stations": stations, "lorries": lorries})