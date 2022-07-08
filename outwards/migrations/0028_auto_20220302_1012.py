# Generated by Django 3.2.8 on 2022-03-02 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outwards', '0027_alter_outward_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='span',
            new_name='time_to_completion',
        ),
        migrations.AlterField(
            model_name='case',
            name='initiator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='case',
            name='nature_of_information_received',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Bank', 'Bank'), ('BO', 'BO'), ('Directors', 'Directors'), ('Accounting', 'Accounting'), ('Invoices', 'Invoices'), ('Agreements', 'Agreements'), ('Contracts', 'Contracts'), ('Others', 'Others')], default='Bank', max_length=65),
        ),
        migrations.AlterField(
            model_name='case',
            name='nature_of_information_requested',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Bank', 'Bank'), ('BO', 'BO'), ('Directors', 'Directors'), ('Accounting', 'Accounting'), ('Invoices', 'Invoices'), ('Agreements', 'Agreements'), ('Contracts', 'Contracts'), ('Others', 'Others')], default='Bank', max_length=65),
        ),
    ]
