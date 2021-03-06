# Generated by Django 3.0.6 on 2021-05-05 07:16

import common.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(blank=True, choices=[('EN', 'English'), ('ES', 'Español')], default='EN', max_length=2, null=True)),
                ('newsletter', models.BooleanField(default=False)),
                ('promotions', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User profile',
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(max_length=32)),
                ('receptor_name', models.CharField(blank=True, max_length=64, null=True, validators=[common.validators.ModelValidators.name])),
                ('phone', models.CharField(blank=True, max_length=10, null=True, validators=[common.validators.ModelValidators.phone])),
                ('zip_code', models.CharField(blank=True, max_length=5, null=True, validators=[common.validators.ModelValidators.zip_code])),
                ('street', models.CharField(max_length=32)),
                ('ext_number', models.CharField(blank=True, max_length=5, null=True)),
                ('int_number', models.CharField(blank=True, max_length=5, null=True)),
                ('reference', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_city_address', to='common.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User address',
                'verbose_name_plural': 'User address',
            },
        ),
    ]
