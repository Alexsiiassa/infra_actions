from django.http import HttpResponse


def index(request):
    data = 'У меня получилось!'
    return HttpResponse(request, data)


def second_page(request):
    return HttpResponse(request, 'А это вторая страница')
