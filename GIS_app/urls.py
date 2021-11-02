from django.urls import path
from . import views

app_name = 'GIS_app' 
urlpatterns = [
    path('', views.index, name='index'),
    path('elevation/', views.elevation, name='elevation'),
    path('home/', views.home, name='home')

]