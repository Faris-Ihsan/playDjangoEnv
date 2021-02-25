import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectUserModel_1184099.settings')


import django
django.setup()

#Faker
import random
from usermodelchallenge_1184099.models import Challenge
from faker import Faker
from random import randrange

fakegen = Faker()


def populate(N=31):
    for entry in range(N):
        #get User for entry
        gender_random = randrange(2)
        if gender_random == 0:
            gender_random = "Female"
        else:
            gender_random = "Male"

        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_gender = str(gender_random)

        challenge = Challenge.objects.get_or_create(first_name=fake_first_name, gender=fake_gender)[0]

        
        #print(fake_first_name)
        #print(gender)

    
if __name__ == '__main__':
    print("populating the database ............ please wait!")
    populate()
    print("Populating Complete!")