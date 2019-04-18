import folium
import os
import json
from interactive_map.settings import BASE_DIR



def get_color(map_data, countries_list):
    """
    function which returns color of the map.
    if name of chosen country is equal to the country name from json file it returns red colour
    for that country, if not it returns blue"""
    # print(map_data['properties']['NAME'])
    # for x in country:
    #     print(f'lista z jsona {x}')
    # print(f'lista panstw{countries_list}')

    for value in countries_list:
        if value in map_data['properties']['NAME']:
            for item in countries_list:
                if item in map_data['properties']['NAME']:
                    return 'red'
    else:
        return 'blue'

#
# def style_function2(countries_list):
#
#     print(countries_list)
#
#     content = folium.GeoJson(
#         data=open(os.path.join(BASE_DIR, "my_map", "static", "my_map", "world.json"), "r",
#                   encoding="utf-8-sig").read())
#     for x in content.data['features']:
#         # print(x['properties']['NAME'])
#
#         return {'fillColor': get_color(x['properties']['NAME'], countries_list),
#         'fillOpacity': 0.5,
#         'color': 'black',
#         'line_opacity': 0.5,
#         'weight': 1}

def style_function1(map_data, countries_list):

    return lambda map_data: dict(fillColor=get_color(map_data, countries_list), weight=1, fillOpacity=0.5,
                                          color='black', line_opacity=0.5)

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

    feature_group = folium.FeatureGroup(name="My map")

    lista = []

    with open(os.path.join(BASE_DIR, "my_map", "static", "my_map", "world.json"), "r", encoding="utf-8-sig") as f:
        map_data = json.load(f)

    # for feature in map_data['features']:
    #     country = feature['properties']['NAME']
    #     lista.append(country)
    #     # print(lista)

    gj = folium.GeoJson(map_data, style_function=style_function1(map_data,countries_list))
    gj.add_to(my_map)
    #
    # feature_group.add_child(folium.GeoJson()
    #
    # # feature_group.add_child(folium.GeoJson(
    # #     data=open(os.path.join(BASE_DIR, "my_map", "static", "my_map", "world.json"), "r", encoding="utf-8-sig").read(),
    # #     style_function=lambda map_data: {
    # #         'fillColor': get_color(map_data, countries_list),
    # #         'fillOpacity': 0.5,
    # #         'color': 'black',
    # #         'line_opacity': 0.5,
    # #         'weight': 1
    # #     }))
    #
    # my_map.add_child(feature_group)

    return my_map.get_root().render()

