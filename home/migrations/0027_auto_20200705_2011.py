# Generated by Django 3.0.6 on 2020-07-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_watchedvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchedvideos',
            name='answer',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='watchedvideos',
            name='query',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
