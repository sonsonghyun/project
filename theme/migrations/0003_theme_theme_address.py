# Generated by Django 4.0.2 on 2022-04-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_remove_theme_theme_photo_theme_photo1_theme_photo2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='theme_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
