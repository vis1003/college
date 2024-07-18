from django.db import models

# Create your models here.

genders = (("M","Male"),("F","Female"))

class Course(models.Model):
    course_code = models.CharField(max_length=10, blank=False, null=False, unique=True)
    course_name = models.CharField(max_length=100, blank=False, null=False)
    course_credits = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.course_name
    
class Student(models.Model):
    student_usn = models.CharField(max_length=10, blank=False, null=False, unique=True)
    student_name = models.CharField(max_length=100, blank=False, null=False)
    student_sem = models.IntegerField(blank=False, null=False)
    student_gender = models.CharField(max_length=1, blank=False, null=False, choices=genders)
    enrolment = models.ManyToManyField(Course)