from django.shortcuts import render
from .models import Station, ParkingLorry, Closure

# Create your views here.

def home(request):
    return render(request, "home.html")

def map(request):
    stations = Station.objects.all()
    lorries = ParkingLorry.objects.all()
    closures = Closure.objects.all()
    print(stations[0].latitude, stations[0].longitude)
    return render(request, "map.html", {"stations": stations, "lorries": lorries, "closures": closures})