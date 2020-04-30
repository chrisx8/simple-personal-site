# Generated by Django 3.0.5 on 2020-04-30 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', help_text='This field sets the Meta Description tag for /projects/. Leave blank to use global Meta Description tag.', max_length=250)),
                ('projects_per_page', models.IntegerField(default=6)),
            ],
            options={
                'verbose_name': '# Projects Config #',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, unique=True, verbose_name='Project Name')),
                ('description', models.TextField(default='', help_text='Write in Markdown format', verbose_name='Project Description')),
                ('url', models.URLField(blank=True, verbose_name='Project URL')),
                ('posted', models.DateField(auto_now_add=True)),
                ('embed', models.ForeignKey(blank=True, help_text='<strong>When printing, only image will show.</strong><br>If both are selected, only embedded media will show on screen.', null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Embed')),
                ('image', models.ForeignKey(blank=True, help_text='If both are selected, only embedded media will show on screen.', null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Image')),
            ],
            options={
                'ordering': ['-posted', 'title'],
            },
        ),
    ]
