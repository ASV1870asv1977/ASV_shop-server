from django.shortcuts import render

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
    }
    return render(request, 'products/products.html', context)


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



