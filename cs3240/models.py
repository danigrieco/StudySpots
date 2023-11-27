from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=700)
    address = map_fields.AddressField(max_length=200)
    admin_approved = models.BooleanField(default=False)
    delete_place = models.BooleanField(default=False)
    locations = [("Central Grounds", "central"),
                 ("North Grounds", "north"),
                 ("South Grounds", "south")]
    location = models.CharField(blank=True, choices=locations, max_length=15)
    def __str__(self):
        return self.name
    def get_suggested_place(location, busy_rating, wifi_outlet_rating):
        suggested_place = Place.objects.filter(admin_approved=True).first()
        return suggested_place
class Review(models.Model):
    Place = models.ForeignKey(Place, on_delete=models.CASCADE)
    busy_rating = models.IntegerField(default = 5)
    wifi_outlet_rating = models.IntegerField(default = 5)
    user = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.choice_text 
