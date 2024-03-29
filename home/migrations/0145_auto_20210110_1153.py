# Generated by Django 3.0.6 on 2021-01-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0144_megaquizinstruction_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='megaquizresult',
            name='day1',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='day2',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='day3',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='day4',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='day5',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='day6',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='day7',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='score',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='time',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='time1',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='time2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='time3',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='time4',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='time5',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='time6',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='megaquizresult',
            name='time7',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
