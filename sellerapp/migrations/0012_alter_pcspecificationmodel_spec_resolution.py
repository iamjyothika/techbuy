# Generated by Django 5.0.2 on 2024-03-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0011_alter_televisionmodels_spec_resolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcspecificationmodel',
            name='spec_resolution',
            field=models.CharField(max_length=30),
        ),
    ]