# Generated by Django 3.0.6 on 2020-07-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20200720_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hometutor',
            name='varified',
        ),
        migrations.AddField(
            model_name='hometutor',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
