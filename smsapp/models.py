from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    choices = (("7:00am to 11:00am","7:00am to 11:00am"),
               ("1:00pm to 5:00pm", "1:00pm to 5:00pm"))
    shift = models.CharField(choices=choices, max_length=200, null=True, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=200)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.name


