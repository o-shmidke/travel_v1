from django import forms

from cities.models import City
from .models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Номер поезда', widget=forms.TextInput(
        attrs={'class': "form-control",
               'placeholder': 'Введите номер поезда'}))
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': "form-control",
               'placeholder': 'Выберите откуда следует поезд'}))
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': "form-control",
               'placeholder': 'Выберите куда следует поезд'}))
    travel_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(
        attrs={'class': "form-control",
               'placeholder': 'Введите время в пути'}))

    class Meta(object):
        model = Train
        fields = ('name', 'from_city', 'to_city', 'travel_time')
