from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('timer/index.html')
    context = {
        'latest_question_list': "",
    }
    return HttpResponse(template.render(context, request))