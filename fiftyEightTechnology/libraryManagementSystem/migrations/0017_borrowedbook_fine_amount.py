# Generated by Django 4.2.11 on 2024-04-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libraryManagementSystem", "0016_rename_language_book_language_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowedbook",
            name="fine_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
