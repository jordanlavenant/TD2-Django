from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Product, ProductItem, ProductAttribute
from django.views.generic import *

# Create your views here.
class HomeView(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    if (self.kwargs.get('param') == '' or self.kwargs.get('param') == None): 
      context['titreh1'] = "Hello DJANGO"
    else:
      context['titreh1'] = f"Bonjour {self.kwargs.get('param')}"
    return context

  def post(self, request, **kwargs):
    return render(request, self.template_name)
  
class AboutView(TemplateView):
  template_name = "home.html"

  def get_context_data(self, **kwargs):
    context = super(AboutView, self).get_context_data(**kwargs)
    context['titreh1'] = "About us..."
    return context
  
  def post(self, request, **kwargs):
    return render(request, self.template_name)
  
class ContactView(TemplateView):
  template_name = "home.html"

  def get_context_data(self, **kwargs):
    context = super(ContactView, self).get_context_data(**kwargs)
    context['titreh1'] = "Contact us..."
    return context
  
  def post(self, request, **kwargs):
    return render(request, self.template_name)

# Product  

class ProductListView(ListView):
  model = Product
  template_name = "products.html"
  context_object_name = "products"
  queryset = Product.objects.all()

  def get_queryset(self):
    return Product.objects.order_by('price_ttc')
  
  def get_context_data(self, **kwargs):
    context = super(ProductListView, self).get_context_data(**kwargs)
    context['titremenu'] = "Liste des Products"
    context['products'] = self.get_queryset()
    return context
  
class ProductDetailView(DetailView):
  model = Product
  template_name = "detailProduct.html"
  context_object_name = "product"

  def get_context_data(self, **kwargs):
    context = super(ProductDetailView, self).get_context_data(**kwargs)
    context['titremenu'] = "Détail Product"
    return context
  
# Product Item

class ProductItemListView(ListView):
  model = ProductItem
  template_name = "productsItem.html"
  context_object_name = "products"
  queryset = ProductItem.objects.all()

  def get_queryset(self):
    return ProductItem.objects.all()
  
  def get_context_data(self, **kwargs):
    context = super(ProductItemListView, self).get_context_data(**kwargs)
    context['titremenu'] = "Liste des Products Item"
    context['products'] = self.get_queryset()
    return context
  
class ProductItemDetailView(DetailView):
  model = ProductItem
  template_name = "detailProductItem.html"
  context_object_name = "product"

  def get_context_data(self, **kwargs):
    context = super(ProductItemDetailView, self).get_context_data(**kwargs)
    context['titremenu'] = "Détail Product Item"
    return context
  
# Product Attribute

class ProductAttributeListView(ListView):
  model = ProductAttribute
  template_name = "productsAttribute.html"
  context_object_name = "products"
  queryset = ProductAttribute.objects.all()

  def get_queryset(self):
    return ProductAttribute.objects.all()
  
  def get_context_data(self, **kwargs):
    context = super(ProductAttributeListView, self).get_context_data(**kwargs)
    context['titremenu'] = "Liste des Products Attribute"
    context['products'] = self.get_queryset()
    return context
  
class ProductAttributeDetailView(DetailView):
  model = ProductAttribute
  template_name = "detailProductAttribute.html"
  context_object_name = "product"

  def get_context_data(self, **kwargs):
    context = super(ProductAttributeDetailView, self).get_context_data(**kwargs)
    context['titremenu'] = "Détail Product Attribute"
    return context