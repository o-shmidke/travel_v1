from django.db import models
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование маршрута', unique=True)
    from_city = models.CharField(max_length=100, verbose_name='Откуда', unique=True)
    to_city = models.CharField(max_length=100, verbose_name='Куда', unique=True)
    across_cities = models.ManyToManyField(Train, blank=True, verbose_name='Через города')
    travel_time = models.IntegerField(verbose_name='Время в пути')

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['name']
