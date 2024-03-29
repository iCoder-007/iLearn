# Generated by Django 3.0.6 on 2020-06-23 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_auto_20200620_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vedios',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('videoTitle', models.CharField(max_length=150)),
                ('videofile', models.FileField(null=True, upload_to='home/videos/', verbose_name='')),
                ('thumbnail', models.ImageField(default='', upload_to='home/images')),
                ('resource', models.FileField(null=True, upload_to='home/resource/', verbose_name='')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('creater', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('videoOfCourse', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Courses')),
            ],
        ),
    ]
