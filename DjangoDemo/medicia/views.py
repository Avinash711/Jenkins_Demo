from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse("<h1> this is V2:::\nHello world! this is first jenkins job!!</h1> ")
