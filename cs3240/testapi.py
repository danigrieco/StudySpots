from django.test import TestCase, Client
from django.urls import reverse
from .models import Place


class PlaceListTestCase(TestCase):
    def setUp(self):
        # Set up the test client
        self.client = Client()

    def test_approved_place_in_template(self):
        place = Place.objects.create(
            name="Test Place",
            details="Test Details",
            address="123 Main St",
            admin_approved=True
        )
        url = reverse('places')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, place.name)
        self.assertContains(response, place.details)
        self.assertContains(response, "https://www.google.com/maps/search/?api=1&query=")

