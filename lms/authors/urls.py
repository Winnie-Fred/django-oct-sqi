from django.urls import path

from . import views

app_name = "authors"

urlpatterns = [
    path("all-authors/", views.all_authors, name="all_authors"),
    path('authors-books/', views.authors_books_view, name="authors_books"),
    path('author-detail/<int:author_pk>', views.author_detail, name="author_detail"),
]