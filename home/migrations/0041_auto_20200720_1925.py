# Generated by Django 3.0.6 on 2020-07-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_auto_20200720_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometutordemo',
            name='homeTutor',
            field=models.CharField(max_length=1000),
        ),
    ]
