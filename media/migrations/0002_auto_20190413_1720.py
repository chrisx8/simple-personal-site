# Generated by Django 2.2 on 2019-04-13 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['name']},
        ),
    ]
