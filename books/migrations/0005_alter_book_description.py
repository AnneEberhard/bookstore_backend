# Generated by Django 4.2 on 2024-06-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_url_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=1500),
        ),
    ]
