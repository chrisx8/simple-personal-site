# Generated by Django 3.1.7 on 2021-03-03 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20210303_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='(no subject)', max_length=300),
        ),
    ]