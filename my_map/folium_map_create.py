
import folium
import os
from interactive_map.settings import BASE_DIR

"""
Function to create interactive map.
This function was used to create 'static map.html'
It is a plain map, which is display on the 'map_create.html'

Then it is called whenever the user fills up the form correctly
It takes the values of the form.
Then it is using geoJson to read 'world.json' file. It takes a coordinates for each country.
Lastly basing on the form's values and json's values it colors the map and return that map.

"""

def map_create_function(lista):

    def get_color(map_data):
        condition = False
        for value in lista:
            if value == map_data['properties']['NAME']:
                condition = True
        if condition == False:
            return 'blue'
        else:
            for z in lista:
                if z == map_data['properties']['NAME']:
                    return 'red'
    mapa = folium.Map(location=None, tiles='Mapbox Bright', no_wrap=True, width=800, height=500)

    feature_group = folium.FeatureGroup(name="My map")

    feature_group.add_child(folium.GeoJson(
        data=open(os.path.join(BASE_DIR, f"my_map/static/my_map/world.json"), "r", encoding="utf-8-sig").read(),
        style_function=lambda map_data: {
            'fillColor': get_color(map_data),
            'fillOpacity': 0.5,
            'color': 'black',
            'line_opacity': 0.5,
            'weight': 1
        }))

    mapa.add_child(feature_group)

    return mapa.save(os.path.join(BASE_DIR, r"my_map/templates/my_map/my_map.html"))
