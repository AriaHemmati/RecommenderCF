from django.urls import path , include
from . import views



urlpatterns = [
    path('home/',views.home , name='home'),
    path('search/',views.search, name='search')
]