# Generated by Django 3.1.6 on 2021-02-09 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactconfig',
            name='from_name',
        ),
    ]