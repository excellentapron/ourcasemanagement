# Generated by Django 3.2.8 on 2021-12-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_alter_board_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='reference',
            field=models.CharField(default='SRC.I.', max_length=12, unique=True),
        ),
    ]