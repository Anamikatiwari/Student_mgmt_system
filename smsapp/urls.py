from django.urls import path
from .views import student_list,course_list
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='courses_list'),
    path('student_detail/<int:id>', views.student_detail, name='student_detail'),
    path('create/', views.create, name='create'),
  
]
