# Generated by Django 3.0.3 on 2020-04-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataforseo', '0005_keywordsearch_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordBulk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=50, verbose_name='Método')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('keywords', models.TextField(blank=True, max_length=250, null=True, verbose_name='Listado de keywords')),
                ('language', models.CharField(blank=True, max_length=70, null=True, verbose_name='Idioma/País')),
                ('result', models.TextField(blank=True, null=True, verbose_name='Resultado')),
                ('user', models.CharField(blank=True, max_length=100, null=True, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'KeywordList',
                'verbose_name_plural': 'KeywordLists',
            },
        ),
    ]