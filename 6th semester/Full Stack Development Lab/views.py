from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.

def myFunc(request):
    return HttpResponse("<h1>My name is Vismitha<h1>")