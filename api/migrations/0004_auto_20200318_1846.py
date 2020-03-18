# Generated by Django 2.2 on 2020-03-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200318_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronacounrty',
            name='active_cases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coronacounrty',
            name='new_cases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coronacounrty',
            name='new_deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coronacounrty',
            name='serious_cases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coronacounrty',
            name='total_cases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coronacounrty',
            name='total_deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coronacounrty',
            name='total_recovered',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackcountry',
            name='active_cases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackcountry',
            name='new_cases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackcountry',
            name='new_deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackcountry',
            name='serious_cases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackcountry',
            name='total_cases',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackcountry',
            name='total_deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackcountry',
            name='total_recovered',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]