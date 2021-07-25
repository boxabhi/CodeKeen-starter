from datetime import date
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        name = request.POST.get('name')
        room_name = request.POST.get('room_name')

        return redirect(f'chat/{room_name}/?name={name}')
    return render(request , 'home.html')


def chat(request , room_name):
    print(room_name)
    context = {'room_name' : room_name}
    return render (request , 'chat.html' , context)