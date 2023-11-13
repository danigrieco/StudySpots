from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Place

class ProfileViewTests(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret1234'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_wrong_login_credentials(self):
        login_status = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(login_status)

    def test_correct_login_credentials(self):
        login_status = self.client.login(**self.credentials)
        self.assertTrue(login_status)
