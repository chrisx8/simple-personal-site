# Generated by Django 2.2.1 on 2019-05-29 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_config', '0003_auto_20190512_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='footer_copyright',
            field=models.CharField(default='Simple Personal Site by chrisx8.', help_text='"&copy; YEAR " always shows. Set this to be the text after "&copy; YEAR "', max_length=250),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='site_url',
            field=models.URLField(default='http://example.com', help_text='Include "http://" or "https://". No trailing slashes. <strong>Effective after restart</strong>', verbose_name='Site URL'),
        ),
    ]