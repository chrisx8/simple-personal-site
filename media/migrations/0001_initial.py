# Generated by Django 2.2 on 2019-04-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('caption', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('video_source', models.CharField(choices=[('youtube', 'YouTube'), ('vimeo', 'Vimeo')], default='', max_length=10)),
                ('video_id', models.CharField(default='', help_text='YouTube video ID is the 11-character string after "watch?v=". Vimeo video ID is the numbers after "vimeo.com/"', max_length=15)),
            ],
        ),
    ]
