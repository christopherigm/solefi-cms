# Generated by Django 3.0.6 on 2021-07-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_grid', '0012_infogriditem_image_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infogriditem',
            name='image_position',
            field=models.CharField(choices=[('top', 'top'), ('bottom', 'bottom'), ('left', 'left'), ('right', 'right')], default='top', max_length=32),
        ),
    ]
