import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectUserModel_1184099.settings')


import django
django.setup()

#Faker
import random
from userModel_app_1184099.models import User
from faker import Faker

fakegen = Faker()


def populate(N=31):
    for entry in range(N):
        #get User for entry

        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

        #print(fake_name)
        #print(fake_first_name)

    
if __name__ == '__main__':
    print("populating the database ............ please wait!")
    populate()
    print("Populating Complete!")