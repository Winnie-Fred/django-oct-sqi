from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("create-book/", views.create_book, name="create_book"),
    path('create-book-manually/', views.create_book_manual, name="create_book_manual"),
    path("list-of-books/", views.book_list, name="all_books"),
    path("book/<int:book_pk>", views.book_detail, name="book_detail"),
    path("update-book/<int:id>", views.update_book, name="update_book"),
    path("confirm-delete/<int:book_id>", views.confirm_delete, name="confirm_delete"),
    path("delete-book/<int:book_id>", views.delete_book, name="delete_book"),
]