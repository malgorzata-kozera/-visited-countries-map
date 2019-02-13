from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('interactive_map/', views.map_create, name='map_create'),
    path('static_map/', views.static_map, name='static_map'),
    path('my_dynamic_map/', views.dynamic_map, name='dynamic_map'),

]
