# djangoGEE/gee/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Maps the root URL to the index view
]
