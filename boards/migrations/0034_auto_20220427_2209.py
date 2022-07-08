# Generated by Django 3.2.8 on 2022-04-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0033_auto_20220427_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='if_other',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='board',
            name='tax_period',
            field=models.CharField(choices=[('2015-2016', '2015-2016'), ('2016-2017', '2016-2017'), ('2017-2018', '2017-2018'), ('2018-2019', '2018-2019'), ('2019-2020', '2019-2020'), ('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('Custom', 'Custom')], default='', max_length=15),
        ),
    ]