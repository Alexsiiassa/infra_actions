from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):
    return HttpResponse(request, 'У меня получилось!')


@require_http_methods(["GET"])
def second_page(request):
    return HttpResponse(request, 'А это вторая страница')
