from django.db import models

class Station(models.Model):
    road = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    display_type = models.CharField(max_length=100, null=True, blank=True)
    extent = models.CharField(max_length=100, null=True, blank=True)
    footer = models.JSONField(null=True) 
    future = models.BooleanField(null=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    isBlocked = models.CharField(max_length=10, null=True, blank=True)
    lorryParkingFeatureIcons = models.JSONField(null=True)
    point = models.CharField(max_length=255, null=True, blank=True)
    routeRecommendation = models.JSONField(null=True)

