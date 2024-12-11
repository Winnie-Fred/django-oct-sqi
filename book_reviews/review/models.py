import os


from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify

from django.utils import timezone


User = get_user_model()

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    year_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class GenreChoices(models.TextChoices):
    FANTASY = "FTSY", "Fantasy"
    SCI_FI = "SCIFI", "Science Fiction"
    MYSTERY_THRILLER = "MYST_THRILL", "Mystery/Thriller"
    ROMANCE = "ROM", "Romance" 
    HISTORICAL_FICTION = "HIST_FIC", "Historical Fiction"
    HORROR = "HORROR", "Horror"
    DYSTOPIAN = "DYST", "Dystopian"
    ADVENTURE = "ADVN", "Adventure"
    BIO_AUTOBIO = "BIO_AUTOBIO", "Biography/Autobiography"
    SELF_HELP = "SELF_HELP", "Self Help"
    HISTORY = "HIST", "History"
    SCIENCE = "SCI", "Science"
    BUSINESS = "BSNS", "Business"


def book_cover_upload_to(instance, filename):
    # Generate a shorter, more manageable file name
    _, ext = os.path.splitext(filename)
    return f"book_covers/{slugify(instance.title)}{ext}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=11, choices=GenreChoices.choices, default=GenreChoices.FANTASY)
    no_of_pages = models.PositiveIntegerField()
    isbn = models.CharField(max_length=255)
    published_on = models.DateField()
    cover_image = models.ImageField(upload_to=book_cover_upload_to)

    def __str__(self):
        return f"{self.title}"

def validate_rating(rating):
    if rating < 1 or rating > 5:
        raise ValidationError("Rating must be between 1 and 5")

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[validate_rating])
    added_on = models.DateTimeField(auto_now_add=True)

    @property
    def edit_is_not_within_time_window(self):
        now = timezone.now()
        time_difference = now - self.added_on
        return time_difference.total_seconds() > (5 * 60)
        

    def __str__(self):
        return f"Review by {self.added_by}"
