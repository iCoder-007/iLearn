# Generated by Django 3.0.6 on 2020-10-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0075_doubtreply_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubtreply',
            name='username',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
