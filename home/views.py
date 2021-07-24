from datetime import date
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .helpers import *


# Abhijeet
# Akash
#Abhhay
# jgab

# beajhj
# jysdbe
# starts


#students.object.filter(student_email__icontains = "@hotmail.com")
#Student.objects.filter(student_email__icontains='@gmail')
# Students.objects.filter(student_email__endswith==".@gmail.com")
# Student.objects.filter(student_email='@hotmail')


# select_related 
# prefetch_related


def home(request):
    return render(request , 'home.html')