from django.shortcuts import render, redirect

from authors.models import Author
from .forms import BookForm

# Create your views here.
def home(request):
    return render(request, "library/home.html")

def create_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("library:home")
        
    context = {"book_create_form": form}
    
    return render(request, "library/create-book.html", context)

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