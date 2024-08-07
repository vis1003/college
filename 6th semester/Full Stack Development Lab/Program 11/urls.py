"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from prog9.views import addProject
from program10.views import StudentDetailView, StudentListGenView
from program11.views import generate_csv_response, generate_pdf_response

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register_student/", addProject),
    path("student_list/",StudentListGenView.as_view()),
    path("student_gen_detail/<int:pk>/",StudentDetailView.as_view()),
    path('generatecsv/', generate_csv_response),
    path('generatepdf/', generate_pdf_response),
]
