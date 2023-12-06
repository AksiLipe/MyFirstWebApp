from django.shortcuts import render

def index(request):
    data = { #Создали словарь
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data) #Обрабатываем запрос и возвращаем шаблон html из папки templates

def about(request):
    return render(request, 'main/about.html') #Обрабатываем запрос и возвращаем шаблон html из папки templates
