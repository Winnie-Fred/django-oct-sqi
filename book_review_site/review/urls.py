from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("book-list/", views.book_list, name="book_list"),
    path("book-detail/<int:book_id>/", views.book_detail, name="book_detail"),
    path("leave-review/<int:book_id>/", views.create_review, name="create_review"),
]