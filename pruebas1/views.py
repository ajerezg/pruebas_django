from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

# Create your views here.

def hola_mundo(request):
    return HttpResponse('Hola Mundo!')
