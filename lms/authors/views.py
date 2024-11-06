from django.shortcuts import render, get_object_or_404

from .models import Author
from library.models import Book

# Create your views here.
def all_authors(request):
    authors = Author.objects.all()
    context = {"all_authors": authors}
    return render(request, "authors/all-authors.html", context)

def authors_books_view(request):
    authors = Author.objects.order_by("-date_of_birth")
    books = Book.objects.all()
    context = {
        "all_authors": authors,
        "all_books": books,
    }
    return render(request, "authors/authors_books.html", context)


def author_detail(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    context = {"author": author}
    return render(request, "authors/author-detail.html", context)