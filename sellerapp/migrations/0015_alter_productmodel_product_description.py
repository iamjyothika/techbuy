# Generated by Django 5.0.2 on 2024-04-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0014_alter_pcspecificationmodel_spec_os'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_description',
            field=models.CharField(max_length=400),
        ),
    ]