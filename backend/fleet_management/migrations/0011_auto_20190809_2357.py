# Generated by Django 2.1.2 on 2019-08-09 23:57

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0010_auto_20190731_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
        ),
    ]
