from django.conf.urls import url
from AppTwo_1184099 import views

urlpatterns =[
    url (r'^$',views.help,name='help'),
]