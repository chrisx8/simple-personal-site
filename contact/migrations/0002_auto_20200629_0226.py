# Generated by Django 3.0.7 on 2020-06-29 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactconfig',
            name='site_owner_email',
        ),
        migrations.RemoveField(
            model_name='contactconfig',
            name='subject',
        ),
        migrations.AddField(
            model_name='contactconfig',
            name='notification_recipient',
            field=models.EmailField(blank=True, help_text='Blank = no notification emails for new messages', max_length=254, verbose_name="Notification recipient's email address"),
        ),
        migrations.AlterField(
            model_name='contactconfig',
            name='from_email',
            field=models.EmailField(blank=True, help_text='Blank = no outgoing emails', max_length=254, verbose_name='Email address shown on outgoing emails'),
        ),
        migrations.AlterField(
            model_name='contactconfig',
            name='from_name',
            field=models.CharField(blank=True, help_text='Blank = no outgoing emails', max_length=50, verbose_name='Name shown on outgoing emails'),
        ),
    ]
