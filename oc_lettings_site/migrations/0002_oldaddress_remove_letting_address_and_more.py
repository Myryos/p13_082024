# Generated by Django 5.1 on 2024-09-09 12:52

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OldAddress",
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
                    "number",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(9999)]
                    ),
                ),
                ("street", models.CharField(max_length=64)),
                ("city", models.CharField(max_length=64)),
                (
                    "state",
                    models.CharField(
                        max_length=2,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "zip_code",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(99999)]
                    ),
                ),
                (
                    "country_iso_code",
                    models.CharField(
                        max_length=3,
                        validators=[django.core.validators.MinLengthValidator(3)],
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="letting",
            name="address",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.CreateModel(
            name="OldLetting",
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
                ("title", models.CharField(max_length=256)),
                (
                    "address",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="oc_lettings_site.oldaddress",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OldProfile",
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
                ("favorite_city", models.CharField(blank=True, max_length=64)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="oc_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Address",
        ),
        migrations.DeleteModel(
            name="Letting",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
