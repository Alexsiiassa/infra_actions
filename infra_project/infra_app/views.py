from django.http import HttpResponse


def index(request):
    text = 'У меня получилось!'
    context = {
        'text_repr': text,
    }
    return HttpResponse(request, context)


def second_page(request):
    return HttpResponse(request, 'А это вторая страница')
