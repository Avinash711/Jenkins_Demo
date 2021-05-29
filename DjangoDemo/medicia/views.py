from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse("<h1> Hello world! this is first jenkins job!!</h1> ")
