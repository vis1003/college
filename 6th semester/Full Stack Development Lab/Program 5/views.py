from django.shortcuts import render

# Create your views here.
def lists(request):
    fruits = ["Apple", "Banana", "Mango"]
    students = ["Sam", "Ram", "James", "Rose"]
    return render(request,"mytemplate.html",{"fruits":fruits,"students":students})
