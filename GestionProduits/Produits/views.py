from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()
    print(products)
    return render(
        request,
        'products.html',
        {'products': products}
    )

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(
        request,
        'product.html',
        {'product': product}
    )