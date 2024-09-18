from django.shortcuts import render

# Create your views here.
def products_list(request):
    products = Product.objects.all()
    print(products)
    return render(
        request,
        'products.html',
        {'products': products}
    )