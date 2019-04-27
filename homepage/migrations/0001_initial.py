# Generated by Django 2.2 on 2019-04-27 22:33

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
                ('about_me', models.TextField(default='', help_text='Write in Markdown format', verbose_name='About Me section')),
                ('resume', models.FileField(blank=True, help_text='Upload resume as a PDF for best compatibility', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
