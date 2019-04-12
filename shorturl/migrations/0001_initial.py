# Generated by Django 2.2 on 2019-04-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('alias', models.CharField(default='', help_text='Example: XYZ is the alias in shortened URL example.com/go/XYZ', max_length=50, primary_key=True, serialize=False)),
                ('full_url', models.URLField(default='')),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['alias'],
            },
        ),
    ]
