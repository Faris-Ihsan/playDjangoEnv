from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em> Aplikasi Kedua Saya_1184099_Faris Muhammad Ihsan </em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render (request,'appTwo/help.html',context=helpdict)
    
