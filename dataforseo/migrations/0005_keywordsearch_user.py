# Generated by Django 3.0.3 on 2020-04-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataforseo', '0004_auto_20200331_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordsearch',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Usuario'),
        ),
    ]
