# Generated by Django 3.0.6 on 2020-07-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20200712_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchedvideos',
            name='watched',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
