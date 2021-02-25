import os

#Configure settings for project
#Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'FirstProject_1184099_FarisMuhammadIhsan.settings')

#Import Settings
import django
django.setup()

#Faker Script
import random
from first_app_1184099.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        #get topics for entry

        top = add_topic()

        #create the fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage
        webpg = Webpage.objects.get_or_create(topic=top,
                                              url=fake_url,
                                              name=fake_name)[0]

        #Create a fake access record for that webpage
        #Create Fake Access Record for that page
        #Could add more of these if you wanted ....
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,
                                                     date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the database ..... Please Wait!")
    populate(2)
    print("Populating Complete!")