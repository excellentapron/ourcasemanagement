# Generated by Django 3.2.8 on 2021-12-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20211118_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='legal_instrument',
            field=models.CharField(choices=[('OECD Model Tax Convention', 'OECD Model Tax Convention'), ('UN Model Tax Convention', 'UN Model Tax Convention'), ('Global Forum Mutual Administrative Assistance Agreement', 'Global Forum Mutual Administrative Assistance Agreement'), ('Global Forum Model Tax Information Exchange Agreement', 'Global Forum Model Tax Information Exchange Agreement'), ('African Tax Administration Forum Mutual Administrative Assistance Agreement', 'African Tax Administration Forum Mutual Administrative Assistance Agreement'), ('Regional instruments and agreements', 'Regional instruments and agreements')], default='OECD Model Tax Convention', max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='progress',
            field=models.CharField(choices=[('Acknowledgement sent', 'Acknowledgement sent'), ('Case rejected', 'Case rejected'), ('Interim report sent', 'Interim report sent'), ('Allocated to SRC Department', 'Allocated to SRC Department'), ('Allocated to Third Party', 'Allocated to Third Party'), ('Partial / Interim Response sent', 'Partial / Interim Response sent'), ('Final Response sent', 'Final Response sent'), ('Partial / Interim Response Received', 'Partial / Interim Response Received'), ('Final Response Received', 'Final Response Received'), ('Case Finalised', 'Case Finalised')], default='OECD Model Tax Convention', max_length=40),
        ),
        migrations.AlterField(
            model_name='topic',
            name='query',
            field=models.CharField(choices=[('Request for Information', 'Request for Information'), ('Automatic Exchange of Information', 'Automatic Exchange of Information'), ('Spontaneous Exchange of Information', 'Spontaneous Exchange of Information')], default='OECD Model Tax Convention', max_length=150),
        ),
    ]
