from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stations/', views.stations, name='Stations')
]