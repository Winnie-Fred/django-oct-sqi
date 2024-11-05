from django.urls import path

from . import views

urlpatterns = [
    path("all-authors/", views.all_authors, name="all_authors"),
    path('authors-books/', views.authors_books_view, name="authors_books"),
]