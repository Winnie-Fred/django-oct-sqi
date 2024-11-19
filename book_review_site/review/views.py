from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Review
from .forms import BookReviewForm

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "review/book-list.html", context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    context = {"book": book, "reviews": reviews}
    return render(request, "review/book-detail.html", context)

def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookReviewForm()
    if request.method == "POST":
        form = BookReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("review:book_list")
    context = {"form": form, "book": book}
    return render(request, "review/create-review.html", context)    
