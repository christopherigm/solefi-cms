# Generated by Django 3.0.6 on 2021-05-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_grid', '0004_infogrid_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='infogriditem',
            name='button_text',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='infogriditem',
            name='hide_on_mobile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='infogriditem',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
