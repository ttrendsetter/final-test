from django.http import HttpResponse
from parser.parser import parse
from django.contrib import messages
# Create your views here.


def parsing(request):
    parse()
    return HttpResponse('Parsing is finished')