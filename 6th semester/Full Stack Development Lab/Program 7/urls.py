"""
URL configuration for sample project.

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

from prog4.views import displaydateoffset
from prog3.views import displaydate
from prog1.views import checkif18, votefromhome
from prog5.views import lists
from prog6.views import homepage, contactpage, aboutpage
from prog7.views import course_search, register
from viva1.views import vivalists
from shownameapp.views import myFunc

urlpatterns = [
    path("admin/", admin.site.urls),
    path("smn/", myFunc),
    path("vote/<int:age>", votefromhome),
    path("check/<int:age>", checkif18),
    path("date/", displaydate),
    path("datetimeoffset/", displaydateoffset),
    path("lists/",lists),
    path("vivalists/",vivalists),
    path("home/", homepage),
    path("about/", aboutpage),
    path("contact/", contactpage),
    path("register/",register),
    path("coursesearch/",course_search)
]
