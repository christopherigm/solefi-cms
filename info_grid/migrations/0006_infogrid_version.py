# Generated by Django 3.0.6 on 2021-05-08 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_grid', '0005_auto_20210507_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='infogrid',
            name='version',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
