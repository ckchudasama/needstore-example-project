# Generated by Django 5.0 on 2024-01-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='youtube_video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
