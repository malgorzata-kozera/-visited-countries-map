
from django.shortcuts import render,redirect
from .forms import CountriesChoice
from .folium_map_create import map_create_function
from django.http import HttpResponse
from .models import MapDatabase


def about(request):
    return render(request, "my_map/about.html")


def home_page(request):
    return render(request, "my_map/home.html")


def static_map(request):
    return render(request, "my_map/static_map.html")


def dynamic_map(request):
    """dynamic_map() takes a database object (map's html in string format) and renders it in a normal html file
    returns html file with created map """
    httpstring = MapDatabase.objects.get(id=1)
    vaule_of_httpstring = httpstring.html_string

    return HttpResponse(vaule_of_httpstring)


def map_create(request):
    """ map_create () takes a chosen options from the form. If form is valid it creates a list with all chosen countries
    then it uses a map_create_function() with that list as an argument to create a map
    next it saves created map as an object in a database."""

    if request.method == 'POST':
        form = CountriesChoice(request.POST)
        if form.is_valid():
            europe = form.cleaned_data.get("Europe")
            asia = form.cleaned_data.get("Asia")
            africa = form.cleaned_data.get("Africa")
            oceania = form.cleaned_data.get("Oceania")
            antarctica = form.cleaned_data.get("Antarctica")
            north_america = form.cleaned_data.get("North_America")
            south_america = form.cleaned_data.get("South_America")

            countries_list = europe+africa+oceania+antarctica+north_america+south_america+asia
            maps_as_string = map_create_function(countries_list)

            my_map_object = MapDatabase(id=1, html_string=maps_as_string)
            my_map_object.save()

            return redirect('created_map')

    else:

        form = CountriesChoice
    return render(request, 'my_map/map_create.html', {'form': form})


def created_map(request):
    return render(request, "my_map/created_map.html")
