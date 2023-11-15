from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200,null=True)
    details = models.CharField(max_length=500,null=True)
    address = map_fields.AddressField(max_length=200,null=True)
    admin_approved = models.BooleanField(default=False)
    avg_busy_rating = models.FloatField(default = 5)
    avg_wifi_outlet_rating = models.FloatField(default = 5)
    def __str__(self):
        return self.name
    def get_suggested_place(location, busy_rating, wifi_outlet_rating):
        suggested_place = Place.objects.filter(admin_approved=True).first()
        return suggested_place
    def get_average_review(self):
        reviews = Review.objects.filter(Place=self)
        total_busy = 0
        total_wifi = 0
        if reviews.exists():
            for review in reviews:
                total_busy += review.busy_rating
                total_wifi += review.wifi_outlet_rating
            avg_busy_rating = round(total_busy/ len(reviews), 2)
            avg_wifi_outlet_rating = round(total_wifi/ len(reviews), 2)
            return avg_busy_rating, avg_wifi_outlet_rating
        return 5, 5


    
class Review(models.Model):
    Place = models.ForeignKey(Place, on_delete=models.CASCADE)
    busy_rating = models.IntegerField(default = 5)
    wifi_outlet_rating = models.IntegerField(default = 5)
    description = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.choice_text 
