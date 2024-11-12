from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("create-book/", views.create_book, name="create_book"),
]