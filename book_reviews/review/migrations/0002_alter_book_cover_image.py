# Generated by Django 5.1.3 on 2024-12-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to='book_cover_upload_to/'),
        ),
    ]
