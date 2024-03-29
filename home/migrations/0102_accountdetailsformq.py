# Generated by Django 3.0.6 on 2020-10-30 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0101_notify_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetailsForMQ',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('upi', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('totalWon', models.IntegerField(default=0)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
