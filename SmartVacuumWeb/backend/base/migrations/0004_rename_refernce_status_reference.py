# Generated by Django 4.1.2 on 2022-10-11 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="status",
            old_name="refernce",
            new_name="reference",
        ),
    ]
