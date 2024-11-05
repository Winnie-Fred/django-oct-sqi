from django.db import models

# Create your models here.

class GenderChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GenderChoices, default=GenderChoices.MALE)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

