# Generated by Django 3.2.8 on 2021-12-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_rename_legal_instrument_topic_instrument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='query',
        ),
        migrations.AddField(
            model_name='board',
            name='query',
            field=models.CharField(choices=[('Request for Information', 'Request for Information'), ('Automatic Exchange of Information', 'Automatic Exchange of Information'), ('Spontaneous Exchange of Information', 'Spontaneous Exchange of Information')], default='Request for Information', max_length=150),
        ),
    ]
