# Generated by Django 4.0.2 on 2022-04-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_title', models.CharField(max_length=200)),
                ('theme_contents', models.CharField(max_length=200)),
                ('theme_photo', models.FileField(upload_to='')),
                ('theme_time', models.CharField(max_length=200)),
                ('theme_num', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
