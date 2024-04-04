from django.shortcuts import render,redirect
from .models import Student, Course
from smsapp.form import StudentForm

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


def create(request): 
    form=StudentForm(request.POST, request.FILES)
    if request.method=='POST':
        # print(request.POST)
        form=StudentForm(request.POST)
        if form.is_valid():
            todo= form.save(commit=False)
            todo.user=request.user
            form.save()
            return redirect('student_detail')
        else:
            form = StudentForm()
    return render(request,'list/create.html',{'form':form})


    
    

