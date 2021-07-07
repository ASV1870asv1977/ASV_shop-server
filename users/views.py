from django.shortcuts import render

# Create your views here.


def login(request):
    ''' Функция - контроллер на отображение шаблона login.html '''

    return render(request, 'users/login.html')


def registration(request):
    ''' Функция - контроллер на отображение шаблона registration.html '''

    return render(request, 'users/registration.html')