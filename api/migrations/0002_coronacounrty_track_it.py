# Generated by Django 2.2 on 2020-03-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coronacounrty',
            name='track_it',
            field=models.BooleanField(default=False),
        ),
    ]
