# Generated by Django 3.0.6 on 2021-07-16 08:22

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_page_img_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageaddress',
            name='local_region',
            field=models.CharField(blank=True, max_length=64, null=True, validators=[common.validators.ModelValidators.name]),
        ),
    ]
