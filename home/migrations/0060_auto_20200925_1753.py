# Generated by Django 3.0.6 on 2020-09-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_test_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='Marked',
            field=models.CharField(default='general', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='transfered',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='test',
            name='Marked',
            field=models.CharField(default='fetured', max_length=10),
        ),
    ]
