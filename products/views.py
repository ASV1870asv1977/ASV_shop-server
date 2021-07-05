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


def products(request):
    ''' Функция - контроллер на отображение шаблона products.html '''
    context = {
        'title': 'GeekShop - Каталог',
        #'products': json_read_product(),
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)


'''
def json_read_product():
     Функция чтения данных по продуктам из файла products.json

    with open('products/fixtures/products.json', 'r', encoding='UTF-8') as f:
        products_list = json.load(f)
    return products_list
'''



