# Generated by Django 3.0.6 on 2020-06-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_courses_coursethumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='creater_name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
