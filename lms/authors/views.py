from django.shortcuts import render

from .models import Author
from library.models import Book

# Create your views here.
def all_authors(request):
    return render(request, "authors/all-authors.html")

def authors_books_view(request):
    authors = Author.objects.order_by("-date_of_birth")
    books = Book.objects.all()
    context = {
        "all_authors": authors,
        "all_books": books,
    }
    return render(request, "authors/authors_books.html", context)