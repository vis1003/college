#shownameapp
from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.

def myFunc(request):
    return HttpResponse("<h1>My name is Vismitha<h1>")

#prog1 app
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def votefromhome(request,age):
    if(age > 60):
        diff = age-60
        return HttpResponse("You can vote from home because you are <b>%s</b> years more than threshold age"%(diff))
    
    else:
        diff = 60-age
        return HttpResponse("You cannot vote from home because you are <b>%s</b> years less than threshold age"%(diff))
    
def checkif18(request,age):
    if(age>=18):
        return HttpResponse("You are eligible to vote as you are <b>%s</b> years more than threshold age"%(age-18))
    
    else:
        return HttpResponse("You are not eligible to voteas you are <b>%s</b> years less than threshold age"%(18-age))
