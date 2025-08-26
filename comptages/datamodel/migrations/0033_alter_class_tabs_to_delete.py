import ast
import json
import django.contrib.postgres.fields
from django.db import migrations, models


def convert_text_to_array(apps, schema_editor):
    ClassModel = apps.get_model("comptages", "Class")
    for obj in ClassModel.objects.all():
        if obj.tabs_to_delete:
            obj.tabs_to_delete_tmp = ast.literal_eval(obj.tabs_to_delete)
            obj.save(update_fields=["tabs_to_delete_tmp"])


def revert_array_to_text(apps, schema_editor):
    ClassModel = apps.get_model("comptages", "Class")
    for obj in ClassModel.objects.all():
        if obj.tabs_to_delete_tmp:
            obj.tabs_to_delete = json.dumps(obj.tabs_to_delete_tmp)
            obj.save(update_fields=["tabs_to_delete"])


class Migration(migrations.Migration):

    dependencies = [
        ("comptages", "0032_fix_classes_values"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="tabs_to_delete_tmp",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=90, null=True),
                default=list,
                size=None,
            ),
        ),
        migrations.RunPython(convert_text_to_array, revert_array_to_text),
        migrations.RemoveField(
            model_name="class",
            name="tabs_to_delete",
        ),
        migrations.RenameField(
            model_name="class",
            old_name="tabs_to_delete_tmp",
            new_name="tabs_to_delete",
        ),
    ]
