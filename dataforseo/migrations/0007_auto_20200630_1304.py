# Generated by Django 3.0.3 on 2020-06-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataforseo', '0006_keywordbulk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordbulk',
            name='keywords',
            field=models.TextField(blank=True, null=True, verbose_name='Listado de keywords'),
        ),
    ]
