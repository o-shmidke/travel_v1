from django import forms
from .models import *


class CityForms(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(
        attrs={'class': "form-control",
               'placeholder': 'Введите название города'}))

    class Meta(object):
        model = City
        fields = ('name',)
