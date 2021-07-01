from django.shortcuts import render
import json
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
        'title': 'GeekShop - Продукты',
        'products': json_read_product(),
    }
    return render(request, 'products/products.html', context)


def json_read_product():
    ''' Функция чтения данных по продуктам из файла products.json'''

    with open('products/fixtures/products.json', 'r', encoding='UTF-8') as f:
        products_list = json.load(f)
    return products_list




# ============ lesson_2 code ========================
''''''
def test_context(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340},
        ]
    }
    return render(request, 'products/test-context.html', context)



