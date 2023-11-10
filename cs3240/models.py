from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200,null=True)
    details = models.CharField(max_length=500,null=True)
    admin_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def get_suggested_place(location, busy_rating, wifi_outlet_rating):
        suggested_place = Place.objects.filter(admin_approved=True).first()

        return suggested_place