# Generated by Django 3.0.6 on 2020-12-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0122_auto_20201228_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='captions',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
    ]