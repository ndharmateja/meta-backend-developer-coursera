from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from demo app")

def hello(request):
    return HttpResponse("<h1>Hello</h1><p>Helllooooo.. la la la</p>")

def re_view(request, id):
    return HttpResponse(f"hello {id}")