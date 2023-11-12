from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200, default="NULL", null=False, blank=False)
    details = models.CharField(max_length=700, default="NULL",null=False, blank=False)
    address = map_fields.AddressField(max_length=200,default ="NULL",null=False, blank=False)
    admin_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
