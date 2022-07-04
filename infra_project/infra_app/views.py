from django.shortcuts import render


def index(request):
    return render(request, 'У меня получилось!')


def second_page(request):
    return render(request, 'А это вторая страница')
