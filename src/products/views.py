from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Product


class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'
    queryset = Product.objects.all().featured()


class ProductFeaturedView(DetailView):
    template_name = 'products/featured-detail.html'
    queryset = Product.objects.all().featured()


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_queryset(self, *args, **kwargs):
    #     # request = self.request
    #     return Product.objects.all()


class ProductView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)
