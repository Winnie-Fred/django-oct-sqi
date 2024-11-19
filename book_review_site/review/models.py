from django.db import models
from django.core.exceptions import ValidationError

def validate_rating(rating):
    if rating < 1 or rating > 5:
        raise ValidationError("Rating must be between 1 and 5")

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[validate_rating,])
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer_name}"
