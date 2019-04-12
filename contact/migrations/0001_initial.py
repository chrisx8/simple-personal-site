# Generated by Django 2.2 on 2019-04-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(default='')),
                ('read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['read', 'timestamp'],
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(default='', help_text='Name of the social media platform', max_length=50)),
                ('username', models.CharField(default='', help_text='Omit @ symbol', max_length=100)),
                ('url', models.URLField(default='', help_text='Link to profile page')),
                ('color', models.CharField(default='3273DC', help_text='Color of social media logo.', max_length=6)),
                ('fa_icon', models.CharField(blank=True, default='', max_length=50, verbose_name='Font Awesome icon class')),
                ('display_at', models.BooleanField(default=False, verbose_name='Display "@" before username')),
                ('show', models.BooleanField(default=True, verbose_name='Show on Home and Contact page')),
            ],
            options={
                'ordering': ['platform', 'username'],
            },
        ),
    ]
