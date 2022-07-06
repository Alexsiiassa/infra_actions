from urllib import response
from django.http import HttpResponse


def index(request):
    return HttpResponse(response, 'У меня получилось!')


def second_page(request):
    return HttpResponse(response, 'А это вторая страница')
