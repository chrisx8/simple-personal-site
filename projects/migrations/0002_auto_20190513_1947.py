# Generated by Django 2.2.1 on 2019-05-13 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_embed'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='video',
        ),
        migrations.AddField(
            model_name='project',
            name='embed',
            field=models.ForeignKey(blank=True, help_text='When both are selected, only embedded media will show.', null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Embed'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ForeignKey(blank=True, help_text='When both are selected, only embedded media will show.', null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Image'),
        ),
    ]