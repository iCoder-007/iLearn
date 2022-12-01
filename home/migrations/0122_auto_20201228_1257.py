# Generated by Django 3.0.6 on 2020-12-28 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0121_practice_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedcomment',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FeedShare',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('feed', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Feed')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedLike',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, default='', max_length=10000, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('feed', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Feed')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]