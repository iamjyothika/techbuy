# Generated by Django 5.0.2 on 2024-03-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_productbrandmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbrandmodel',
            name='brand_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
