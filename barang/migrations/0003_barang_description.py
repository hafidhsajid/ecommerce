# Generated by Django 3.0.2 on 2023-01-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_auto_20230128_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
