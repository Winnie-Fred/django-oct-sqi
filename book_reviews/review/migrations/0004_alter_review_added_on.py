# Generated by Django 5.1.3 on 2024-12-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
