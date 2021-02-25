from django.shortcuts import render
from django.http import HttpResponse
from usermodelchallenge_1184099.models import Challenge

# Create your views here.
def challenges(request):
    user_list = Challenge.objects.filter(gender='Male').order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'challenges.html',context=user_dict)
