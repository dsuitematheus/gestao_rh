from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'), #estamos dando um nome para nossa url
]