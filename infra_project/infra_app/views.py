from django.http import HttpResponse


def index(request):
    return HttpResponse(
        request, 'infra_project/index.html', 'У меня получилось!'
    )


def second_page(request):
    return HttpResponse(
        request, 'infra_project/second_page.html', 'А это вторая страница'
    )
