import folium
import os
from interactive_map.settings import BASE_DIR


def get_color(country_data, countries_list):
    """
    function which returns color of the map.
    if name of chosen country is equal to the country name from json file it returns red colour
    for that country, if not it returns blue"""

    for x in countries_list:
        if x in country_data['properties']['NAME']:
            return 'red'
    else:
        return 'blue'


def map_create_function(countries_list):
    """
    Function to create interactive map.
    This function was used to create 'static map.html'
    It is a plain map, which is display on the 'map_create.html'

    Then it is called whenever the user fills up the form correctly
    It takes the list with a values of the form as an argument.
    Then it is using geoJson to read 'world.json' file. It takes a coordinates for each country.
    Lastly basing on the form's values and json's values it colors the map and return that map
    (map's html in a string format)."""

    my_map = folium.Map(location=None, tiles='Mapbox Bright', no_wrap=True, width=800, height=500)

    # creating and adding a features to the map

    gj = folium.GeoJson(
        data=open(os.path.join(BASE_DIR, "my_map", "static", "my_map", "world.json"), "r", encoding="utf-8-sig").read(),
        style_function=lambda country_data: {
            'fillColor': get_color(country_data, countries_list),
            'fillOpacity': 0.5,
            'color': 'black',
            'line_opacity': 0.5,
            'weight': 1
        })
    gj.add_to(my_map)
    return my_map.get_root().render()
