# Generated by Django 3.2.8 on 2021-12-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outwards', '0003_auto_20211211_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outward',
            name='reference',
            field=models.CharField(default='SRC.I.', max_length=30, unique=True),
        ),
    ]
