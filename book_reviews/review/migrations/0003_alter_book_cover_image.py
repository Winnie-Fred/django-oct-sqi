# Generated by Django 5.1.3 on 2024-12-02 10:57

import review.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to=review.models.book_cover_upload_to),
        ),
    ]
