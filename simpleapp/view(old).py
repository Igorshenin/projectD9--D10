from django.shortcuts import render
from django.views.generic import ListView, DetailView  # импортируем класс получения деталей объекта
from .models import Product
#

class ProductsList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'


# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта. в нём будет