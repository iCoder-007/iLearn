# Generated by Django 3.0.6 on 2020-11-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0114_auto_20201117_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetailsformq',
            name='upi',
            field=models.CharField(blank=True, default='None', max_length=500, null=True),
        ),
    ]
