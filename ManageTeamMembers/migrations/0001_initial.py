# Generated by Django 4.1 on 2022-08-05 02:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('admin', models.BooleanField()),
            ],
        ),
    ]
