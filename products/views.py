from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product, ProductCategory

# Create your views here.
# функции = контроллеры = въюхи


def index(request):
    ''' Функция - контроллер на отображение шаблона index.html '''
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    ''' Функция - контроллер на отображение шаблона products.html '''
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 3) # Что и в каком количестве отобразить на странице
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)




