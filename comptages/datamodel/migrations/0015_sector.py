# Generated by Django 3.2.4 on 2021-10-15 08:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comptages", "0014_count_tjm"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sector",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.GeometryField(
                        blank=True, null=True, srid=2056
                    ),
                ),
            ],
            options={
                "db_table": "sector",
            },
        ),
    ]
