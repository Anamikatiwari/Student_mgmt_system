from django.shortcuts import render
from .models import Student, Course

def student_list(request):
    students = Student.objects.all()
    return render(request, 'list/student_list.html', {'students': students})

def course_list(request):
    courses=Course.objects.all()
    return render(request, 'list/courses_list.html', {'courses':courses})

def student_detail(request, id):
    course= Course.objects.get(id=id)
    student= course.student.all()
    return render(request, 'list/student_detail.html', {'student':student})
    

