from django.contrib import admin
from .models import Author
from library.models import Book

# Register your models here.

class BookInline(admin.TabularInline):  # or admin.StackedInline
    model = Book
    extra = 1  # Number of empty forms to display in the inline (1 by default)

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)