from django.http import HttpResponse
from django.contrib import messages
from .parser import parse
# Create your views here.


def parsing(request):
    parse()
    return HttpResponse('Parsing is finished')