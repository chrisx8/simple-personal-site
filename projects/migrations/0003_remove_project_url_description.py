# Generated by Django 2.2.1 on 2019-06-08 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190513_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url_description',
        ),
    ]
