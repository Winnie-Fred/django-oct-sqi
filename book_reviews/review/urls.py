from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("book/<int:book_pk>", views.book_detail, name="book_detail"),
    path("leave-a-review/<int:book_pk>/", views.create_review, name="create_review"),
    path("edit-review/<int:book_pk>/<int:review_pk>", views.edit_review, name="edit_review"),
    path("confirm-delete/<int:book_pk>/<int:review_pk>", views.confirm_delete, name="confirm_delete"),
    path("delete-review/<int:book_pk>/<int:review_pk>", views.delete_review, name="delete_review"),
    
]