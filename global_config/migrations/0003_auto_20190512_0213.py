# Generated by Django 2.2.1 on 2019-05-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_config', '0002_auto_20190501_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='site_url',
            field=models.URLField(default='', help_text='Include "http://" or "https://". No trailing slashes. <strong>Effective after restart</strong>', verbose_name='Site URL'),
        ),
    ]