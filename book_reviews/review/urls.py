from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
]