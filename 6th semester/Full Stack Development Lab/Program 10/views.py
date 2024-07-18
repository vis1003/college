from django.shortcuts import render
from django.views import generic

from program10.models import Student

# Create your views here.

class StudentListGenView(generic.ListView):
    model = Student
    template_name = "student_list_view.html"

class StudentDetailView(generic.DetailView):
    model = Student
    template_name="student_gen_detail.html"
