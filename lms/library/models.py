from django.db import models

from authors.models import Author

# Create your models here.
# title, author, number of pages, published on

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    no_of_pages = models.PositiveIntegerField()
    published_on = models.DateField()

    def __str__(self):
        return f"{self.title}"
