# Generated by Django 3.0.6 on 2021-05-08 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_page_dns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='version',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
