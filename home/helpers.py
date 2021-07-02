
from django.db.models.query import QuerySet
from django.db.models.query_utils import InvalidQuery
from faker import Faker
fake = Faker()

from .models import *
import random
import datetime

def generate_fake_data():
    for i in range(0 , 20):
        departments = Department.objects.all()
        rand_index = random.randint(0 ,len(departments))

        student_obj = Student.objects.create(
            student_name = fake.name(),
            student_age = random.randint(18 , 54),
            student_dob = datetime.date.today(),
            student_email = fake.email(),
            department = departments[rand_index-1]
        )
        print('Student created')
        skills = list(Skills.objects.all())
        random.shuffle(skills)
        print(skills)
        
        random_list_count =  random.randint(0 , len(skills)-1)
        print(random_list_count)
        for skill in skills[0:random_list_count] :
            skill_obj = Skills.objects.get(id = skill.id)
            student_obj.skills.add(skill_obj)

            print('Student skill added ')
            print(student_obj)


        
Student uuid
134F-3497GH-BJ77
id 1 , 2 , 3 , 4 

depart 1 , 2 , 3 , 4

Inven
1 , 2 , 3 , 4, 5

primary_key = 