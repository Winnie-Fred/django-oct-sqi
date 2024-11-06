from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_debut_year(year):
    current_year = timezone.now().year
    print(current_year)
    if year < 1700 or year > current_year:
        raise ValidationError("Invalid debut year")

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    debut_year = models.IntegerField(validators=[validate_debut_year])


    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title