# Generated by Django 3.0.6 on 2020-10-10 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0071_auto_20201010_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doubtliked',
            name='doubt',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Doubt'),
        ),
    ]
