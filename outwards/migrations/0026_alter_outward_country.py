# Generated by Django 3.2.8 on 2022-02-23 05:50

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('outwards', '0025_rename_date_closed_case_date_process_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outward',
            name='country',
            field=django_countries.fields.CountryField(default='Select country', max_length=2),
        ),
    ]
