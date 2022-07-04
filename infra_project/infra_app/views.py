from django.http import HttpResponse


def index(request):
    real_count = 1
    text_repe = 'У меня получилось!'
    return HttpResponse(request, real_count, text_repe)


def second_page(request):
    real_count = 1
    text_repe = 'А это вторая страница'
    return HttpResponse(request, real_count, text_repe)
