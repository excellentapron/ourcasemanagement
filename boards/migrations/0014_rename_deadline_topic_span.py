# Generated by Django 3.2.8 on 2022-02-09 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0013_auto_20220209_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='deadline',
            new_name='span',
        ),
    ]
