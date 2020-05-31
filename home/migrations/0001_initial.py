# Generated by Django 3.0.6 on 2020-05-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(blank=True, help_text='Write in Markdown format', verbose_name='About Me section')),
                ('resume', models.FileField(blank=True, help_text='Upload resume as a PDF for best compatibility', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='My Site', max_length=50)),
                ('site_url', models.URLField(default='http://example.com', help_text='Include "http://" or "https://". No trailing slashes.', verbose_name='Site URL')),
                ('description', models.CharField(blank=True, default='', help_text='This field sets the global Meta Description tag.', max_length=250)),
                ('header_title', models.CharField(default='My Site', max_length=250)),
                ('header_subtitle', models.CharField(blank=True, max_length=250)),
                ('footer_copyright', models.CharField(default='Simple Personal Site by chrisx8.', help_text='"&copy; YEAR " always shows. Set this to be the text after "&copy; YEAR "', max_length=250)),
            ],
            options={
                'verbose_name': '# Site Info #',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(default='', help_text='Name of the social media platform', max_length=50)),
                ('url', models.URLField(default='', help_text='Link to profile page', verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Social Media Link',
                'ordering': ['platform'],
            },
        ),
    ]