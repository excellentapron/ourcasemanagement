# Generated by Django 3.2.8 on 2022-02-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outwards', '0013_case_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='deadline',
            field=models.CharField(choices=[('Acknowledgement sent', 'Alpha'), ('Case rejected', 'Beta'), ('Interim report sent', 'Gamma'), ('Allocated to SRC Department', 'Epsilon'), ('Allocated to Third Party', 'lambda'), ('Partial / Interim Response sent', 'Miu'), ('Final Response sent', 'Jared')], default='Acknowledgement sent', max_length=35),
        ),
    ]