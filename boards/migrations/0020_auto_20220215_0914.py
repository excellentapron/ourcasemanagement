# Generated by Django 3.2.8 on 2022-02-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0019_alter_board_tax_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='instrument',
            field=models.CharField(choices=[('OECD Model Tax Convention', 'OECD Model Tax Convention'), ('UN Model Tax Convention', 'UN Model Tax Convention'), ('Global Forum Mutual Administrative Assistance Agreement', 'Global Forum Mutual Administrative Assistance Agreement'), ('Global Forum Model Tax Information Exchange Agreement', 'Global Forum Model Tax Information Exchange Agreement'), ('African Tax Administration Forum Mutual Administrative Assistance Agreement', 'African Tax Administration Forum Mutual Administrative Assistance Agreement'), ('Regional instruments and agreements', 'Regional instruments and agreements')], default='OECD Model Tax Convention', max_length=100),
        ),
        migrations.AlterField(
            model_name='board',
            name='query',
            field=models.CharField(choices=[('Request for Information', 'Request for Information'), ('Automatic Exchange of Information', 'Automatic Exchange of Information'), ('Spontaneous Exchange of Information', 'Spontaneous Exchange of Information'), ('Tax Examination Abroad', 'Tax Examination Abroad'), ('Joint Audit', 'Joint Audit'), ('Industry Wide Exchange of Information', 'Industry Wide Exchange of Information')], default='OECD Model Tax Convention', max_length=150),
        ),
        migrations.AlterField(
            model_name='board',
            name='tax_period',
            field=models.CharField(default='', max_length=15),
        ),
    ]