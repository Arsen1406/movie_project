# Generated by Django 4.0.5 on 2022-06-08 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0019_remove_director_direktor_mail_director_director_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
