from django.test import TestCase
from my_map.models import MapDatabase


class MapDatabaseTest(TestCase):

    def setUp(self):
        MapDatabase.objects.create(html_string='some string')

    def test_map_object_create(self):
        """Test that new database (map string) object has been created"""
        test_string = MapDatabase.objects.get(html_string='some string')
        self.assertEqual(str(test_string), 'map_string')

    def test_map_value(self):
        """Test if new value of html_string is correct"""
        test_string = MapDatabase.objects.get(html_string='some string')
        self.assertEqual(test_string.html_string, 'some string')
