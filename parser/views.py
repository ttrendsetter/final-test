from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def parsing(request):
    return HttpResponse('Parsing is started')