# Generated by Django 3.2.8 on 2021-12-11 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20211211_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='legal_instrument',
            new_name='instrument',
        ),
    ]