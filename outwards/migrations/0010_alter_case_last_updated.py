# Generated by Django 3.2.8 on 2021-12-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outwards', '0009_alter_case_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]