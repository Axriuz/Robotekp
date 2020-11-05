# Generated by Django 2.2.6 on 2020-02-05 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='multimedia',
            fields=[
                ('IDMultimedia', models.CharField(db_column='IDMultimedia', max_length=30, primary_key=True, serialize=False)),
                ('URL_Video', models.CharField(db_column='URL_Video', max_length=30)),
                ('URL_Imagen', models.CharField(db_column='URL_Imagen', max_length=30)),
            ],
            options={
                'db_table': 'multimedia',
                'managed': False,
            },
        ),
    ]