# Generated by Django 3.0.6 on 2020-10-10 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0073_auto_20201010_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doubtreply',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.DoubtReply'),
        ),
    ]
