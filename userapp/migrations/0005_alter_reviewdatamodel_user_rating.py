# Generated by Django 5.0.2 on 2024-05-07 11:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_remove_cartdatamodel_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewdatamodel',
            name='user_rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
