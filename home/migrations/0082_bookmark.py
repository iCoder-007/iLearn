# Generated by Django 3.0.6 on 2020-10-11 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0081_auto_20201011_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookMark',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Updates')),
            ],
        ),
    ]
