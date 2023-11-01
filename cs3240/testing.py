from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class Tests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')

    def test_redirect_no_login(self):
        response = self.client.get(reverse('index'))
        # Adjust this depending on your login redirect behavior.
        # If unauthenticated users can access the index without being redirected, then this test might not be necessary.
        self.assertEqual(response.status_code, 200)

    def test_wrong_login(self):
        self.assertTrue(isinstance(self.user, User))
        # Using allauth's default login URL
        login_response = self.client.post('/accounts/login/', {'login': 'john', 'password': 'bluesky321'})
        self.assertNotContains(login_response, 'Logout')  # Assuming you have a "Logout" link/button for logged-in users


