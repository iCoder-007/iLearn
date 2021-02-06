# Generated by Django 3.0.6 on 2020-10-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0096_auto_20201026_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='MegaQuizeInstruction',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('winner1price', models.IntegerField(default=600)),
                ('winner2price', models.IntegerField(default=250)),
                ('winner3price', models.IntegerField(default=150)),
                ('instruction', models.CharField(blank=True, default='', max_length=100000, null=True)),
                ('delay', models.IntegerField(default=0)),
                ('cancel', models.BooleanField(default=False)),
                ('reason', models.CharField(blank=True, default='', max_length=100000, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
