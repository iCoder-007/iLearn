# Generated by Django 3.0.6 on 2020-12-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0126_auto_20201229_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='subjects',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='practiceenglish',
            name='subjects',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
