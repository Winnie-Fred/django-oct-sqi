from django.urls import path

from . import views

urlpatterns = [
    path("all-authors/", views.all_authors, name="all_authors"),
]