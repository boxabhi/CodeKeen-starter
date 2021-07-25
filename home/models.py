from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.department_name


class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.skill_name



class Student(models.Model):
    student_name = models.CharField(max_length = 100)
    student_age = models.IntegerField()
    student_dob = models.DateField()
    student_email = models.EmailField()
    department = models.ForeignKey(Department , on_delete=models.SET_DEFAULT , default="Any department" , null=True , blank=True)
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return self.student_email



# class Room(models.Model):
#     room = CharField

# class Chat():
#     room = ForeignKey
#     sender message = 

