# Generated by Django 3.2.3 on 2021-06-04 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("blog", "0001_initial"),
        ("blog", "0002_auto_20210101_2157"),
        ("blog", "0003_delete_blogconfig"),
    ]

    dependencies = [
        ("media", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "tag",
                    models.CharField(
                        default="", max_length=50, primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "ordering": ["tag"],
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "article_id",
                    models.SlugField(
                        primary_key=True, serialize=False, verbose_name="Article ID"
                    ),
                ),
                ("title", models.CharField(default="", max_length=250, unique=True)),
                ("subtitle", models.CharField(blank=True, default="", max_length=250)),
                (
                    "content",
                    models.TextField(default="", help_text="Write in Markdown"),
                ),
                ("last_edited", models.DateField(auto_now=True)),
                (
                    "embed",
                    models.ForeignKey(
                        blank=True,
                        help_text="<strong>When printing, only image will show.</strong><br>If both are selected, only embedded media will show on screen.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="media.embed",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="<strong>When printing, only image will show.</strong><br>If both are selected, only embedded media will show on screen.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="media.image",
                    ),
                ),
                ("tag", models.ManyToManyField(blank=True, to="blog.Tag")),
            ],
            options={
                "ordering": ["-last_edited", "title"],
            },
        ),
    ]
