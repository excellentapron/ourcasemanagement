# Generated by Django 3.2.8 on 2022-04-27 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0032_auto_20220426_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='point_of_contact_surname',
            new_name='others',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='point_of_contact_title',
        ),
    ]
