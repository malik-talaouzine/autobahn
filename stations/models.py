from django.db import models

class Station(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)  # Allows NULL
    subtitle = models.CharField(max_length=255, null=True, blank=True)  # Allows NULL
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    display_type = models.CharField(max_length=100, null=True, blank=True)  # Allows NULL
    extent = models.CharField(max_length=100, null=True, blank=True)  # Allows NULL
    footer = models.JSONField(null=True)  # Allows NULL
    future = models.BooleanField(null=True)  # Allows NULL
    icon = models.CharField(max_length=255, null=True, blank=True)  # Allows NULL
    isBlocked = models.CharField(max_length=10, null=True, blank=True)  # Allows NULL
    lorryParkingFeatureIcons = models.JSONField(null=True)  # Allows NULL
    point = models.CharField(max_length=255, null=True, blank=True)  # Allows NULL
    routeRecommendation = models.JSONField(null=True)  # Allows NULL

    def __str__(self):
        return self.title if self.title else 'No Title'
