# Generated by Django 3.0.6 on 2020-09-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_categories_mytest_test_testcart_testimage_testresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
