from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from authors.models import Author
from .models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    return render(request, "library/home.html")

@login_required
def create_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("library:home")
        
    context = {"book_create_form": form}
    
    return render(request, "library/create-book.html", context)

@login_required
def create_book_manual(request):
    form = BookForm()
    authors = Author.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("library:home")
        
    context = {"form": form, "authors": authors}
    return render(request, "library/create-book-manual.html", context)

def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book-list.html", {"all_the_books": books})

def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return render(request, "library/book-detail.html", {"book": book})

@login_required
def update_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.user != book.added_by:
        return redirect("authentication:log_in")
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("library:all_books")
    context = {
        "book": book,
        "form": form,
    }
    return render(request, "library/book-update.html", context)

@login_required
def confirm_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user != book.added_by:
        return redirect("authentication:log_in")
    context = {"book": book}
    return render(request, "library/confirm-delete.html", context)

@login_required
def delete_book(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, pk=book_id)
        if request.user != book.added_by:
            return redirect("authentication:log_in")
        book.delete()
    return redirect("library:all_books")
