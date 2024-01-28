# Generated by Django 5.0.1 on 2024-01-28 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("applications", "0003_delete_endpoint"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApplicationConfig",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("page_size", models.PositiveIntegerField(default=15)),
                (
                    "application",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="config",
                        to="applications.application",
                    ),
                ),
            ],
            options={
                "db_table": "app_config",
            },
        ),
    ]
