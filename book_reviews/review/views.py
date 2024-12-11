from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, "review/book-list.html", {"books": books})


def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    reviews = Review.objects.filter(book=book)
    return render(request, "review/book-detail.html", {"book": book, "reviews": reviews})

@login_required
def create_review(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("review:book_detail", args=[book_pk]))
    context = {"book": book, "form": form}
    return render(request, "review/create-review.html", context)

@login_required
def edit_review(request, book_pk, review_pk):
    book = get_object_or_404(Book, pk=book_pk)
    review = get_object_or_404(Review, pk=review_pk)
    form = ReviewForm(instance=review)
    if request.user != review.added_by:
        messages.error(request, "You do not have permission to edit that review.")
        return redirect("review:book_list")
    
    if review.edit_is_not_within_time_window:
        messages.error(request, "5 minutes have passed since you left the review, you can no longer edit it.")
        return redirect(reverse("review:book_detail", args=[book_pk]))
    
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(reverse("review:book_detail", args=[book_pk]))
    context = {"book": book, "form": form, "review": review}
    return render(request, "review/edit-review.html", context)

@login_required
def confirm_delete(request, book_pk, review_pk):
    book = get_object_or_404(Book, pk=book_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user != review.added_by:
        messages.error(request, "You do not have permission to delete that review.")
        return redirect("review:book_list")
    context = {"book": book, "review": review}
    return render(request, "review/confirm-delete.html", context)

@login_required
def delete_review(request, book_pk, review_pk):
    get_object_or_404(Book, pk=book_pk)
    if request.method == "POST":
        review = get_object_or_404(Review, pk=review_pk)
        if request.user != review.added_by:
            messages.error(request, "You do not have permission to delete that review.")
            return redirect("review:book_list")
        review.delete()
    return redirect(reverse("review:book_detail", args=[book_pk]))
