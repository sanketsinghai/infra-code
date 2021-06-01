from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/urlshort/', home),
]