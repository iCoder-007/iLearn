# Generated by Django 3.0.6 on 2020-08-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_auto_20200816_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesttution',
            name='Payment',
            field=models.IntegerField(default=0),
        ),
    ]
