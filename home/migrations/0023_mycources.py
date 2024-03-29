# Generated by Django 3.0.6 on 2020-07-02 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_courses_ratedby'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCources',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=-1)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Courses')),
            ],
        ),
    ]
