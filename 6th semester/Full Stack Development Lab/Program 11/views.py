import csv
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

from program10.models import Student

# Create your views here.

def generate_csv_response(request):
    queryset = Student.objects.all() # Get data from your models
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="student_data.csv"'
    writer = csv.writer(response)
    # Write header row based on model fields using List comprehension
    writer.writerow([field.name for field in queryset.model._meta.fields])
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field.name) for field in queryset.model._meta.fields])
    return response


def generate_pdf_response(request):
    queryset = Student.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_pdfdata.pdf"'
    # Create PDF document
    pdf = canvas.Canvas(response)
    y = 800 # Initial y position for writing text
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, y, "Student Data")
    # Write data
    pdf.setFont("Helvetica", 10)
    y -= 30 # Move down for data rows
    for obj in queryset:
        data = f"Name: {obj.student_name}, USN: {obj.student_usn}, Sem: {obj.student_sem}" # Customize based on your model fields
       
        if y < 50:  # If we're near the bottom of the page, start a new page
            pdf.showPage()
            y = 800
            pdf.setFont("Helvetica", 10)
       
        pdf.drawString(100, y, data)
        y -= 15  # Move down for next row
    pdf.showPage()
    pdf.save()
    return response
