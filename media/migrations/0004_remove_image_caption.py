# Generated by Django 2.2.1 on 2019-05-31 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_delete_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='caption',
        ),
    ]