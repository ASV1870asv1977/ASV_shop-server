from django.shortcuts import render
import json
from products.models import Product, ProductCategory
# Create your views here.
# функции = контроллеры = въюхи


def index(request):
    ''' Функция - контроллер на отображение шаблона index.html '''
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    ''' Функция - контроллер на отображение шаблона products.html '''
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    else:
        context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)




