# Generated by Django 5.0.2 on 2024-04-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdatamodel',
            name='cart_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reviewdatamodel',
            name='user_review',
            field=models.TextField(max_length=255),
        ),
    ]