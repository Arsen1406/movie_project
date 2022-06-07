# Generated by Django 4.0.5 on 2022-06-06 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_alter_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', '€'), ('USD', 'Dollars'), ('RUB', '₽')], default='RUB', max_length=3),
        ),
    ]
