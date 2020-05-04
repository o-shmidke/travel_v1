from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CityForms
from .models import City


def home(request):
    cities = City.objects.all()
    paginator = Paginator(cities, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cities/home.html', {"object_list": page_obj})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForms
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')
    success_message = "Город успешно добавлен"
    login_url = '/login/'


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForms
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')
    success_message = "Город успешно изменен"
    login_url = '/login/'


class CityDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город удален')
        return self.post(request, *args, *kwargs)
