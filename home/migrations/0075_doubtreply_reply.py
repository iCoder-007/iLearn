# Generated by Django 3.0.6 on 2020-10-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0074_auto_20201010_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubtreply',
            name='reply',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
