# Generated by Django 5.1.6 on 2025-03-26 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("film", "0002_alter_film_cover_filmvideo_film_media"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="filmvideo",
            table="film_video",
        ),
    ]
