# Generated by Django 5.0.2 on 2024-04-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0015_alter_productmodel_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_description',
            field=models.TextField(max_length=255),
        ),
    ]
