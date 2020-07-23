# Generated by Django 3.0.6 on 2020-07-22 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20200721_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewCourse',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(default='', max_length=500)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('reviewOfCourse', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Courses')),
            ],
        ),
    ]
