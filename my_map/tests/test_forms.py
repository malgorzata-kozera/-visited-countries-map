from django.test import TestCase
from my_map.forms import CountriesChoice


class TestClass(TestCase):

    def test_form_empty(self):
        """Test that empty form is valid"""
        form_data = {}
        form = CountriesChoice(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_notempty(self):
        """Test that data form is valid"""
        form_data = {'Poland': 'Poland'}
        form = CountriesChoice(data=form_data)
        self.assertTrue(form.is_valid())
