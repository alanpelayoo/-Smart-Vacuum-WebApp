# Generated by Django 4.1.2 on 2022-10-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
