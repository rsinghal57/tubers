# Generated by Django 3.2.9 on 2021-12-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
