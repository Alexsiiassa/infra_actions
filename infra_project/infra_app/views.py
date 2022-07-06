from django.http import HttpResponse


def index(request):
    return (request, 'У меня получилось!')


def second_page(request):
    return (request, 'А это вторая страница')
