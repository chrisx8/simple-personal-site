# Generated by Django 3.1.4 on 2021-01-01 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='id',
            new_name='article_id',
        ),
    ]
