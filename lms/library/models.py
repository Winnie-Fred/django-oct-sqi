from django.db import models
from django.contrib.auth import get_user_model

from authors.models import Author

User = get_user_model()

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    no_of_pages = models.PositiveIntegerField()
    published_on = models.DateField()
    cover_image = models.ImageField(upload_to="book_cover_images/", blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
