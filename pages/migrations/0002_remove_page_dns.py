# Generated by Django 3.0.6 on 2021-05-06 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='dns',
        ),
    ]
