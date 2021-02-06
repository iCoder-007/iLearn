# Generated by Django 3.0.6 on 2020-12-30 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0127_auto_20201230_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedcomment',
            name='feed',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Feed'),
        ),
        migrations.AlterField(
            model_name='feedcomment',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
