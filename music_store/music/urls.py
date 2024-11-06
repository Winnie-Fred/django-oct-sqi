from django.urls import path

from . import views

app_name = "music"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("artists_listing/", views.artists_listing, name="artists_listing"),
    path("albums_listing/", views.albums_listing, name="albums_listing"),
]