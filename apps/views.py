from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, CreateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'orders/index.html'


class AboutView(TemplateView):
    template_name = 'orders/about.html'


class GetFormView(CreateView):
    template_name = 'orders/contact.html'

