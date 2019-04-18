import pytest
from my_map.folium_map_create import map_create_function, get_color,style_function1
import folium
import os
from interactive_map.settings import BASE_DIR
import json


class TestClass(object):

    def test_map_create(self):
        pass
    def test_read_json(self):
        pass
    def test_feature_group(self):
        pass
    def test_render_root(self):
        pass

    # def test_get_colour(self):
    #     countries_list = ['Poland', 'Germany', 'Japanese']
    #     with open(os.path.join(BASE_DIR, "my_map", "static", "my_map", "world.json"), "r", encoding="utf-8-sig") as f:
    #         tracks = json.load(f)
    #         # for x in tracks['features']['properties']['NAME']:
    #
    #         assert get_color(tracks, countries_list) == 'red'
    #
    # def test_style_function(self):
    #     countries_list = ['Poland', 'Germany', 'Japanese']
    #
    #     with open(os.path.join(BASE_DIR, "my_map", "static", "my_map", "world.json"), "r", encoding="utf-8-sig") as f:
    #         tracks = json.load(f)
    #     # for x in tracks['features']['properties']['NAME']:
    #
    #         assert lambda tracks: style_function1(tracks,countries_list)== dict(fillColor='red', weight=1, fillOpacity=0.5,
    #                                       color='black', line_opacity=0.5)
    #
    # def test_style_function_not_in(self):
    #
    #     countries_list = ['zsa', 'lala', 'dupa']
    #
    #     with open(os.path.join(BASE_DIR, "my_map", "static", "my_map", "world.json"), "r", encoding="utf-8-sig") as f:
    #         tracks = json.load(f)
    #
    #         assert style_function1(tracks, countries_list) == dict(fillColor='blue', weight=1, fillOpacity=0.5,
    #                                                                          color='black', line_opacity=0.5)
