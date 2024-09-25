from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('home', views.HomeView.as_view(template_name='home.html')),
    path('home/<param>', views.HomeView.as_view(template_name='home.html')),
    path('about', views.AboutView.as_view(template_name='home.html')),
    path('contact', views.ContactView.as_view(template_name='home.html')),

    # Product
    path("products",views.ProductListView.as_view(), name="product-list"),
    path("products/<pk>",views.ProductDetailView.as_view(), name="product-detail"),

    # Product Item
    path("productsitem",views.ProductItemListView.as_view(), name="productitem-list"),
    path("productsitem/<pk>",views.ProductItemDetailView.as_view(), name="productitem-detail"),

    # Product Attribute
    path("productsattribute",views.ProductAttributeListView.as_view(), name="productattribute-list"),
    path("productsattribute/<pk>",views.ProductAttributeDetailView.as_view(), name="productattribute-detail"),
]