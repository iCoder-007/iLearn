# Generated by Django 3.0.6 on 2020-10-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0080_auto_20201011_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='disc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='updates',
            name='discHindi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='updates',
            name='title',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='updates',
            name='titleHindi',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
