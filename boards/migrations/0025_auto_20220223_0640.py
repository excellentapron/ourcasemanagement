# Generated by Django 3.2.8 on 2022-02-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0024_alter_topic_date_closed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='nature_of_information',
            new_name='nature_of_information_received',
        ),
        migrations.AddField(
            model_name='topic',
            name='nature_of_information_requested',
            field=models.CharField(choices=[('Bank', 'Bank'), ('BO', 'BO'), ('Directors', 'Directors'), ('Accounting', 'Accounting'), ('Invoices', 'Invoices'), ('Agreements', 'Agreements'), ('Contracts', 'Contracts'), ('Others', 'Others')], default='Bank', max_length=30),
        ),
    ]