# Generated by Django 4.1 on 2023-11-05 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0009_review_avg_rating_review_number_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='number_rating',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
