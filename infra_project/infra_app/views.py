from django.http import HttpResponse


def index(request):
    return HttpResponse(request, 'infra_project/index.html')


def second_page(request):
    return HttpResponse(request, 'А это вторая страница')
