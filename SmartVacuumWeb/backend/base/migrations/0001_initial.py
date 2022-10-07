# Generated by Django 4.1.2 on 2022-10-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
        ),
    ]