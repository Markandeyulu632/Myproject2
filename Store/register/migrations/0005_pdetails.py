# Generated by Django 3.0.7 on 2020-08-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0004_delete_storeusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]