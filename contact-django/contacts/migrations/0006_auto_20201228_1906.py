# Generated by Django 3.1.4 on 2020-12-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20201228_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='created'),
        ),
    ]