# Generated by Django 3.0.7 on 2020-07-23 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_delete_loginusers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StoreUsers',
        ),
    ]
