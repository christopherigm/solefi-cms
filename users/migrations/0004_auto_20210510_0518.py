# Generated by Django 3.0.6 on 2021-05-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210510_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
