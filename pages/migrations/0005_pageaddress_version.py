# Generated by Django 3.0.6 on 2021-05-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210508_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageaddress',
            name='version',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
