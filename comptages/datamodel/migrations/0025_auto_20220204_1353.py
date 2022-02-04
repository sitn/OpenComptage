# Generated by Django 3.2.5 on 2022-02-04 12:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('comptages', '0024_category_trash'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelclass',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='modelclass',
            name='id_model',
            field=models.ForeignKey(db_column='id_model', on_delete=django.db.models.deletion.DO_NOTHING, to='comptages.model'),
        ),
        migrations.AlterUniqueTogether(
            name='modelclass',
            unique_together=set(),
        ),
    ]
