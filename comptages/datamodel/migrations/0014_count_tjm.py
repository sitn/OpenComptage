# Generated by Django 3.2.4 on 2021-10-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comptages", "0013_auto_20211001_0643"),
    ]

    operations = [
        migrations.AddField(
            model_name="count",
            name="tjm",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
