
from django.shortcuts import render, redirect
from .forms import CountriesChoice
from .folium_map_create import map_create_function
from django.http import HttpResponse

wynik_mapy=""


def about(request):
    return render(request, "my_map/about.html")


def home_page(request):
    return render(request, "my_map/home.html")


def static_map(request):
    return render(request, "my_map/static_map.html")



def dynamic_map(request):

    global wynik_mapy

    return HttpResponse(wynik_mapy)
    # return render(request, "my_map/my_map.html")



def map_create(request):

    lista = []

    form = CountriesChoice
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

            lista = europe+africa+oceania+antarctica+north_america+south_america+asia

            print("Lista - views: ", lista)

            global wynik_mapy

            wynik_mapy = map_create_function(lista)


            return redirect('created_map')
    else:

        form = CountriesChoice
    return render(request, 'my_map/map_create.html', {'form': form})


def created_map(request):

    # global wynik_mapy
    # s = Template(wynik_mapy).safe_substitute(code="We Says Thanks!")
    #
    # context={'mapa':s}
    return render(request, "my_map/created_map.html")
