# Generated by Django 3.0.6 on 2020-06-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='varified',
            field=models.CharField(default='False', max_length=150),
        ),
    ]
