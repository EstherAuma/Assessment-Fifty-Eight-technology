# Generated by Django 4.2.11 on 2024-04-05 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("libraryManagementSystem", "0012_alter_book_genre"),
    ]

    operations = [
        migrations.CreateModel(
            name="OverdueBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fine_amount",
                    models.DecimalField(decimal_places=2, default=10.0, max_digits=10),
                ),
                (
                    "borrowed_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="libraryManagementSystem.borrowedbook",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
