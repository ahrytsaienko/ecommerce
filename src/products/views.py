from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'


class ProductView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

