from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView
from .forms import AdvertisementForm
from .models import Advertisement


# Create your views here.

class MainPage(ListView):
    model = Advertisement
    template_name = 'advertisement/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная станица'
        context['advertisements'] = Advertisement.objects.all()[:3]
        return context


class ShowAllAdvert(ListView):
    model = Advertisement
    template_name = 'advertisement/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все объявления'
        context['advertisements'] = Advertisement.objects.all()
        return context


class Search(ListView):
    model = Advertisement
    template_name = 'advertisement/index.html'
    extra_context = {
        'title': 'Поиск'
    }
    context_object_name = 'advertisements'

    def get_queryset(self):
        return Advertisement.objects.filter(title__iregex=self.request.GET.get('search'))


class PageView(DetailView):
    model = Advertisement
    template_name = 'advertisement/advertisement.html'
    slug_url_kwarg = 'advertisement_slug'
    context_object_name = 'advertisement'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['advertisement'].title
        return context


class AddPage(FormView):
    form_class = AdvertisementForm
    template_name = 'advertisement/form.html'
    success_url = reverse_lazy('main_page')
    extra_context = {
        'title': 'Добавить объявление'
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
