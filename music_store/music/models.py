from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    debut_year = models.IntegerField()

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title