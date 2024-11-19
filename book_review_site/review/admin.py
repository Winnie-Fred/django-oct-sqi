from django.contrib import admin

from .models import Review, Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)