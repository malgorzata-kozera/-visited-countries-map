from interactive_map.settings import BASE_DIR
import os
import json


def select_options(continent):
    """
    Function to create a form 'CountriesChoice' values.
    It is using a json file('country_by_continent.json').
    It sorts a countries' names by continent and saves it as an lists for all continents.
    Function returns options for all continent.
    """
    options_europe = []
    options_asia = []
    options_north_america = []
    options_south_america = []
    options_oceania = []
    options_antarctica = []
    options_africa = []

    with open(os.path.join(BASE_DIR, "my_map","static","my_map","coutry_by_continent.json"), mode='r') as file:
        content = json.load(file)
        for x in content:
            if x['continent'] == 'Europe':
                 options_europe.append((x['country'], x['country']))
            if x['continent'] == 'Asia':
                options_asia.append((x['country'], x['country']))
            if x['continent'] == 'Africa':
                options_africa.append((x['country'], x['country']))
            if x['continent'] == 'Antarctica':
                options_antarctica.append((x['country'], x['country']))
            if x['continent'] == 'Oceania':
                options_oceania.append((x['country'], x['country']))
            if x['continent'] == 'South America':
                options_south_america.append((x['country'], x['country']))
            if x['continent'] == 'North America':
                options_north_america.append((x['country'], x['country']))

    if continent == 'Europe':
        # print (options_europe)
        return options_europe
    elif continent == 'Asia':
        # print (options_asia)
        return options_asia
    elif continent == 'Africa':
        # print(options_africa)
        return options_africa
    elif continent == 'Antarctica':
        # print(options_antarctica)
        return options_antarctica
    elif continent == 'Oceania':
        # print(options_oceania)
        return options_oceania
    elif continent == 'South America':
        # print(options_south_america)
        return options_south_america
    elif continent == 'North America':
        # print(options_north_america)
        return options_north_america
