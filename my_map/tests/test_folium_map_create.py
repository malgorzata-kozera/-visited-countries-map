import pytest
from my_map.folium_map_create import get_color
import os
from interactive_map.settings import BASE_DIR
import json


class TestClass(object):

    def test_get_colour(self):
        """test that map's color is blue and red"""
        countries_list = ['Poland', 'Germany', 'Japanese']
        with open(os.path.join(BASE_DIR, 'my_map', 'static', 'my_map', 'world.json'), 'r', encoding="utf-8-sig") as f:
            map_data = json.load(f)
        for item in map_data['features']:
            assert get_color(item, countries_list) == 'red' or 'blue'


    def test_get_colour_only_blue_when_countries_list_is_empty(self):
        """test that map's color is blue when the countries list is empty"""
        countries_list = []
        with open(os.path.join(BASE_DIR, 'my_map', 'static', 'my_map', 'world.json'), 'r', encoding="utf-8-sig") as f:
            map_data = json.load(f)
        for item in map_data['features']:
            assert get_color(item, countries_list) == 'blue'
