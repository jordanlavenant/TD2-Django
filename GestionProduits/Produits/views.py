from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from .forms import ContactUsForm, ProductForm, ProductAttributeForm, ProductItemForm
from .models import Product, ProductItem, ProductAttribute, ProductAttributeValue
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.

class ConnectView(LoginView):
  template_name = 'login.html'
  
  def post(self, request, **kwargs):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
      login(request, user)
      return render(request, 'home.html',{'titreh1':"hello "+username+", you're connected"})
    else:
      return render(request, 'register.html')

class RegisterView(TemplateView):
  template_name = 'register.html'

  def post(self, request, **kwargs):
    username = request.POST.get('username', False)
    mail = request.POST.get('mail', False)
    password = request.POST.get('password', False)
    user = User.objects.create_user(username, mail, password)
    user.save()
    if user is not None and user.is_active:
      return render(request, 'login.html')
    else:
      return render(request, 'register.html')

class DisconnectView(TemplateView):
  template_name = 'logout.html'

  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)

# Home

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
  
def ContactView(request):
  titreh1 = "Contact us !"
  if request.method=='POST':
    form = ContactUsForm(request.POST)
    if form.is_valid():
      send_mail(
        subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
        message=form.cleaned_data['message'],
        from_email=form.cleaned_data['email'],
        recipient_list=['admin@monprojet.com'],
      )
      return redirect("email-sent")
  else:
    form = ContactUsForm()
  return render(request, "contact/contact.html", {'titreh1':titreh1, 'form':form})

def EmailSentView(request):
  return render(request, "contact/email-sent.html", {'titreh1':"Email sent"})

# Product  
class ProductListView(ListView):
  model = Product
  template_name = "products/products.html"
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
  template_name = "products/detailProduct.html"
  context_object_name = "product"

  def get_context_data(self, **kwargs):
    context = super(ProductDetailView, self).get_context_data(**kwargs)
    context['titremenu'] = "Détail Product"
    return context
  
class ProductCreateView(CreateView):
  model = Product
  form_class=ProductForm
  template_name = "products/new-product.html"

  def form_valid(self, form: BaseModelForm):
    product = form.save()
    return redirect('product-detail', product.id)

class ProductUpdateView(UpdateView):
  model = Product
  form_class=ProductForm
  template_name = "products/update-product.html"

  def form_valid(self, form: BaseModelForm):
    product = form.save()
    return redirect('product-detail', product.id)

class ProductDeleteView(DeleteView):
  model = Product
  template_name = "products/delete-product.html"
  success_url = reverse_lazy('product-list')

# Product Item

class ProductItemListView(ListView):
  model = ProductItem
  template_name = "productsItem/productsItem.html"
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
  template_name = "productsItem/detailProductItem.html"
  context_object_name = "product"

  def get_context_data(self, **kwargs):
    context = super(ProductItemDetailView, self).get_context_data(**kwargs)
    context['titremenu'] = "Détail Product Item"
    return context
  
# Product Attribute

@method_decorator(login_required, name='dispatch')
class ProductAttributeListView(ListView):
  model = ProductAttribute
  template_name = "productsAttribute/productsAttribute.html"
  context_object_name = "productattributes"

  def get_queryset(self ):
    return ProductAttribute.objects.all()
  
  def get_context_data(self, **kwargs):
    context = super(ProductAttributeListView, self).get_context_data(**kwargs)
    context['titremenu'] = "Liste des attributs"
    return context
  
class ProductAttributeDetailView(DetailView):
  model = ProductAttribute
  template_name = "productsAttribute/detailProductAttribute.html"
  context_object_name = "productattribute"

  def get_context_data(self, **kwargs):
    context = super(ProductAttributeDetailView, self).get_context_data(**kwargs)
    context['titremenu'] = "Détail attribut"
    context['values']=ProductAttributeValue.objects.filter(product_attribute=self.object).order_by('position')
    return context