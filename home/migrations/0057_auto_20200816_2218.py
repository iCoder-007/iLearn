# Generated by Django 3.0.6 on 2020-08-16 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_requesttution_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometutor',
            name='unlockedHT',
            field=models.IntegerField(default=0),
        ),
    ]
