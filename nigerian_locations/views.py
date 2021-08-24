from django.shortcuts import render
from django.http import HttpResponse

# /products -> index
def index(request):
    return HttpResponse("Hello world")

def add(request):
    return HttpResponse("New app")
