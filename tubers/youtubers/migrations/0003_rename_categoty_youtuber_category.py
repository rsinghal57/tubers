# Generated by Django 3.2.9 on 2021-12-07 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20211207_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtuber',
            old_name='categoty',
            new_name='category',
        ),
    ]
