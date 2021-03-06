from django.test import TestCase, Client
from django.urls import reverse
from my_map.models import MapDatabase


class PagesTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        """Test that the index page works"""
        url = reverse('home')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        """Test that the about page works"""
        url = reverse('about')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_map_create_page(self):
        """Test that the map_create page works"""
        url = reverse('map_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_created_map_page(self):
        """Test that the created_map page works"""
        url = reverse('created_map')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_dynamic_map_page(self):
        """Test that the dynamic_map page works"""
        http_string = MapDatabase(html_string="some string")
        http_string.save()
        url = reverse('dynamic_map')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)