from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TrainForm

from .models import *


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'trains/home.html', {"object_list": page_obj})


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'object'
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('train:home')
    success_message = "Поезд успешно добавлен"
    login_url = '/login/'


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('train:home')
    success_message = "Поезд успешно изменен"
    login_url = '/login/'


class TrainDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Train
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('train:home')
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд удален')
        return self.post(request, *args, *kwargs)
