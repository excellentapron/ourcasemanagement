# Generated by Django 3.2.8 on 2022-07-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outwards', '0030_auto_20220428_1011'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OutwardDocument',
        ),
        migrations.RenameField(
            model_name='outward',
            old_name='end_date',
            new_name='end_tax_period',
        ),
        migrations.RenameField(
            model_name='outward',
            old_name='if_other',
            new_name='if_other_tax_type',
        ),
        migrations.RenameField(
            model_name='outward',
            old_name='start_date',
            new_name='start_tax_period',
        ),
        migrations.AddField(
            model_name='outward',
            name='document',
            field=models.FileField(default='', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='case',
            name='others',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='case',
            name='point_of_contact_email',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='case',
            name='point_of_contact_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='case',
            name='point_of_contact_telephone1',
            field=models.CharField(blank=True, default='0123430000', max_length=150),
        ),
        migrations.AlterField(
            model_name='case',
            name='point_of_contact_telephone2',
            field=models.CharField(blank=True, default='0123430001', max_length=150),
        ),
        migrations.AlterField(
            model_name='outward',
            name='tax_period',
            field=models.CharField(choices=[('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('Custom', 'Custom')], default='', max_length=15),
        ),
    ]
