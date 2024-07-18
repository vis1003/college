from django.contrib import admin
from program10.models import Course, Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name','student_usn','student_sem','student_gender')

admin.site.register(Course)