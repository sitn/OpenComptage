# Generated by Django 3.2.4 on 2021-08-20 11:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('comptages', '0006_auto_20210820_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classcategory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
