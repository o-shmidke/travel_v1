from django.db import models
from cities.models import City
from django.core.exceptions import ValidationError


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Номер поезда")
    from_city = models.ForeignKey(City, verbose_name='Откуда', on_delete=models.CASCADE, related_name='from_city')
    to_city = models.ForeignKey(City, verbose_name='Куда', on_delete=models.CASCADE, related_name='to_city')
    travel_time = models.IntegerField(verbose_name='Время в пути')

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['name']

    def __str__(self):
        return "Поезд №{} из {} в {}".format(self.name, self.from_city, self.to_city)

    def clean(self, *args, **kwargs):
        if self.from_city == self.to_city:
            raise ValidationError('Измените пункт отправления/прибытия')
        qs = Train.objects.filter(from_city=self.from_city,
                                  to_city=self.to_city,
                                  travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Измените время в пути')

        return super(Train, self).clean(*args, **kwargs)
