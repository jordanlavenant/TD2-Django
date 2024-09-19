from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('<int:product_id>', views.product, name="product"),
    path('<int:product_id>/update', views.update, name="product_update"),
    path('<int:product_id>/delete', views.delete, name="product_update"),
    path('add', views.add, name="product_add"),
]