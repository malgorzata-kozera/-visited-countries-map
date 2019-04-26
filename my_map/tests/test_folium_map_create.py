import pytest
from my_map.folium_map_create import map_create_function, get_color,style_function1
import folium
import os
from interactive_map.settings import BASE_DIR
import json


class TestClass(object):

    def test_get_colour(self):
        countries_list = ['Poland', 'Germany', 'Japanese']
        with open(os.path.join(BASE_DIR, 'my_map', 'static', 'my_map', 'world.json'), 'r', encoding="utf-8-sig") as f:
            map_data = json.load(f)
        for item in map_data['features']:
            assert get_color(item, countries_list) == 'red' or 'blue'
