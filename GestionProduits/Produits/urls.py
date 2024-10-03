from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('home', views.HomeView.as_view(template_name='home.html'), name="home"),
    path('home/<param>', views.HomeView.as_view(template_name='home.html'), name="home"),
    path('about', views.AboutView.as_view(template_name='home.html'), name="about"),
    path('contact', views.ContactView, name="contact"),
    path('email-sent', views.EmailSentView, name="email-sent"),

    # Login / Logout
    path('login/', views.ConnectView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('logout/', views.DisconnectView.as_view(), name="logout"),

    # Product
    path("product",views.ProductListView.as_view(), name="product-list"),
    path("product/<pk>",views.ProductDetailView.as_view(), name="product-detail"),
    path("product/add/",views.ProductCreateView.as_view(), name="product-add"),
    path("product/<pk>/update/",views.ProductUpdateView.as_view(), name="product-update"),
    path("product/<pk>/delete/",views.ProductDeleteView.as_view(), name="product-delete"),

    # Product Item
    # path("productsitem",views.ProductItemListView.as_view(), name="productitem-list"),
    # path("productsitem/<pk>",views.ProductItemDetailView.as_view(), name="productitem-detail"),

    # Product Attribute
    path("productsattribute",views.ProductAttributeListView.as_view(), name="productattribute-list"),
    path("productsattribute/<pk>",views.ProductAttributeDetailView.as_view(), name="productattribute-detail"),
    path("productsattribute/<pk>",views.ProductAttributeDetailView.as_view(), name="productattribute-update"),
    path("productsattribute/<pk>",views.ProductAttributeDetailView.as_view(), name="productattribute-delete"),
]