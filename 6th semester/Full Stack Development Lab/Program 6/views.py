from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse(render(request, 'home.html'))

def contactpage(request):
    return HttpResponse(render(request, 'contact.html'))

def aboutpage(request):
    return HttpResponse(render(request, 'about.html'))
