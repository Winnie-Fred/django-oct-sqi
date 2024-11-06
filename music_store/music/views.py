from django.shortcuts import render

from .models import Artist, Album

# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def artists_listing(request):
    all_artists = Artist.objects.order_by("debut_year")
    context = {"artists": all_artists}
    return render(request, "music/artists.html", context)

def albums_listing(request):
    all_albums = Album.objects.order_by("release_date")
    context = {"albums": all_albums}
    return render(request, "music/albums.html", context)