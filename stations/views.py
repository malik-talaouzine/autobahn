from django.shortcuts import render
from .models import Station, ParkingLorry, Closure, Warning, Roadwork

# Create your views here.

def home(request):
    return render(request, "home.html")

def map(request):
    stations = Station.objects.all()
    lorries = ParkingLorry.objects.all()
    closures = Closure.objects.all()
    warnings = Warning.objects.all()
    roadworks = Roadwork.objects.all()
    return render(request, "map.html", {"stations": stations, "lorries": lorries, "closures": closures, "warnings": warnings, "roadworks": roadworks})