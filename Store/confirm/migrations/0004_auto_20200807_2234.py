# Generated by Django 3.0.7 on 2020-08-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0003_psumitems_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psumitems',
            name='status',
            field=models.CharField(default='Open', max_length=20),
        ),
    ]
