from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200,null=True)
    details = models.CharField(max_length=500,null=True)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    admin_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
