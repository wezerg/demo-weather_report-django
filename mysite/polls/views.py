from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def blop(request):
    return HttpResponse("Hello, world. You're at the polls blop.")