# Generated by Django 4.1 on 2023-11-03 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0007_review_reviewer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviewer_user',
            new_name='review_user',
        ),
    ]