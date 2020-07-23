# Generated by Django 3.0.6 on 2020-07-18 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0035_courses_sub_category2'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTutor',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('classes', models.CharField(max_length=50)),
                ('varified', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('salaryL', models.IntegerField()),
                ('salaryH', models.IntegerField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]