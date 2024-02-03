from django.shortcuts import render
# Where we create oour routes
# Create your views here.
from django.http import HttpResponse #res.json- in javascript

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")