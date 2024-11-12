from django import forms 

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "no_of_pages", "published_on", "cover_image"]
        