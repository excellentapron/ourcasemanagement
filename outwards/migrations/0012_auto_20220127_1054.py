# Generated by Django 3.2.8 on 2022-01-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outwards', '0011_auto_20211214_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='instrument',
        ),
        migrations.AddField(
            model_name='outward',
            name='instrument',
            field=models.CharField(choices=[('OECD Model Tax Convention', 'OECD Model Tax Convention'), ('UN Model Tax Convention', 'UN Model Tax Convention'), ('Global Forum Mutual Administrative Assistance Agreement', 'Global Forum Mutual Administrative Assistance Agreement'), ('Global Forum Model Tax Information Exchange Agreement', 'Global Forum Model Tax Information Exchange Agreement'), ('African Tax Administration Forum Mutual Administrative Assistance Agreement', 'African Tax Administration Forum Mutual Administrative Assistance Agreement'), ('Regional instruments and agreements', 'Regional instruments and agreements')], default='OECD Model Tax Convention', max_length=100),
        ),
        migrations.AlterField(
            model_name='case',
            name='progress',
            field=models.CharField(choices=[('Acknowledgement sent', 'Acknowledgement sent'), ('Case rejected', 'Case rejected'), ('Interim report sent', 'Interim report sent'), ('Allocated to SRC Department', 'Allocated to SRC Department'), ('Allocated to Third Party', 'Allocated to Third Party'), ('Partial / Interim Response sent', 'Partial / Interim Response sent'), ('Final Response sent', 'Final Response sent'), ('Partial / Interim Response Received', 'Partial / Interim Response Received'), ('Final Response Received', 'Final Response Received'), ('Case Finalised', 'Case Finalised')], default='Acknowledgement sent', max_length=40),
        ),
        migrations.AlterField(
            model_name='outward',
            name='query',
            field=models.CharField(choices=[('Request for Information', 'Request for Information'), ('Automatic Exchange of Information', 'Automatic Exchange of Information'), ('Spontaneous Exchange of Information', 'Spontaneous Exchange of Information'), ('Tax Examination Abroad', 'Tax Examination Abroad'), ('Joint Audit', 'Joint Audit'), ('Industry Wide Exchange of Information', 'Industry Wide Exchange of Information')], default='OECD Model Tax Convention', max_length=150),
        ),
    ]