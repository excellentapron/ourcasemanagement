# Generated by Django 3.2.8 on 2021-12-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20211211_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='reference',
            field=models.CharField(default='SRC.I.', max_length=30, unique=True),
        ),
    ]
