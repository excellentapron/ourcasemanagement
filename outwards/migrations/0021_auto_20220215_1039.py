# Generated by Django 3.2.8 on 2022-02-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outwards', '0020_auto_20220215_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outward',
            name='nature_of_information',
        ),
        migrations.AddField(
            model_name='case',
            name='nature_of_information',
            field=models.CharField(choices=[('Bank', 'Bank'), ('BO', 'BO'), ('Directors', 'Directors'), ('Accounting', 'Accounting'), ('Invoices', 'Invoices'), ('Agreements', 'Agreements'), ('Contracts', 'Contracts'), ('Others', 'Others')], default='Bank', max_length=30),
        ),
        migrations.AlterField(
            model_name='case',
            name='progress',
            field=models.CharField(choices=[('Acknowledgement sent', 'Acknowledgement sent'), ('Case rejected', 'Case rejected'), ('Interim report sent', 'Interim report sent'), ('Allocated to SRC Department', 'Allocated to SRC Department'), ('Allocated to Third Party', 'Allocated to Third Party'), ('Partial / Interim Response sent', 'Partial / Interim Response sent'), ('Final Response sent', 'Final Response sent'), ('Partial / Interim Response Received', 'Partial / Interim Response Received'), ('Final Response Received', 'Final Response Received'), ('Case Finalised', 'Case Finalised')], default='Bank', max_length=40),
        ),
        migrations.AlterField(
            model_name='case',
            name='span',
            field=models.CharField(choices=[('3 Days', '3 days'), ('30 days', '30 days'), ('60 days', '60 days'), ('90 days', '90 days'), ('120 days', '120 days'), ('180 days', '180 days'), ('360 days', '360 days')], default='Bank', max_length=35),
        ),
        migrations.AlterField(
            model_name='case',
            name='taxpayer_status',
            field=models.CharField(choices=[('Not Registered', 'Not Registered'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('In Good Standing', 'In Good Standing'), ('Non-Compliant', 'Non-Compliant'), ('Struck Off', 'Struck Off'), ('Dissolved', 'Dissolved')], default='Bank', max_length=40),
        ),
        migrations.AlterField(
            model_name='outward',
            name='instrument',
            field=models.CharField(choices=[('OECD Model Tax Convention', 'OECD Model Tax Convention'), ('UN Model Tax Convention', 'UN Model Tax Convention'), ('Global Forum Mutual Administrative Assistance Agreement', 'Global Forum Mutual Administrative Assistance Agreement'), ('Global Forum Model Tax Information Exchange Agreement', 'Global Forum Model Tax Information Exchange Agreement'), ('African Tax Administration Forum Mutual Administrative Assistance Agreement', 'African Tax Administration Forum Mutual Administrative Assistance Agreement'), ('Regional instruments and agreements', 'Regional instruments and agreements')], default='Bulk', max_length=100),
        ),
        migrations.AlterField(
            model_name='outward',
            name='query',
            field=models.CharField(choices=[('Request for Information', 'Request for Information'), ('Automatic Exchange of Information', 'Automatic Exchange of Information'), ('Spontaneous Exchange of Information', 'Spontaneous Exchange of Information'), ('Tax Examination Abroad', 'Tax Examination Abroad'), ('Joint Audit', 'Joint Audit'), ('Industry Wide Exchange of Information', 'Industry Wide Exchange of Information')], default='Bulk', max_length=150),
        ),
        migrations.AlterField(
            model_name='outward',
            name='query_type',
            field=models.CharField(choices=[('Bulk', 'Bulk'), ('Group', 'Group'), ('Single', 'Single')], default='Bulk', max_length=25),
        ),
        migrations.AlterField(
            model_name='outward',
            name='tax_type',
            field=models.CharField(choices=[('Income Tax', 'Income Tax'), ('Value Added Tax', 'Value Added Tax'), ('Payroll Taxes', 'Payroll Taxes'), ('Excise Tax', 'Excise Tax'), ('Other Tax', 'Other Tax')], default='Bulk', max_length=100),
        ),
    ]
