from django.shortcuts import render

# Create your views here.
# функции = контроллеры = въюхи

def index(request):
    ''' Функция - контроллер на отображение шаблона index.html '''

    return render(request, 'products/index.html')

def products(request):
    ''' Функция - контроллер на отображение шаблона index.html '''

    return render(request, 'products/products.html')
