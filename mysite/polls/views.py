from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': "",
    }
    return HttpResponse(template.render(context, request))

def blop(request):
    return HttpResponse("Hello, world. You're at the polls blop.")