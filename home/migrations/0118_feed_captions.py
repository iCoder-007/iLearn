# Generated by Django 3.0.6 on 2020-12-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0117_feedcomment_savedfeed'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='captions',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
