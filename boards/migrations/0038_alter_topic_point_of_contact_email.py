# Generated by Django 3.2.8 on 2022-06-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0037_alter_topic_point_of_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='point_of_contact_email',
            field=models.CharField(default='', max_length=150),
        ),
    ]
