# Generated by Django 3.0.5 on 2020-05-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование маршрута')),
                ('from_city', models.CharField(max_length=100, unique=True, verbose_name='Откуда')),
                ('to_city', models.CharField(max_length=100, unique=True, verbose_name='Куда')),
                ('travel_time', models.IntegerField(verbose_name='Время в пути')),
                ('across_cities', models.ManyToManyField(blank=True, to='trains.Train', verbose_name='Через города')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ['name'],
            },
        ),
    ]
