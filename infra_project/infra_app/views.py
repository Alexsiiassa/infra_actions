from django.http import HttpResponse


def index(request):
    return HttpResponse(request, 'У меня получилось!')


def second_page(request):
    return HttpResponse(request, 'А это вторая страница')
