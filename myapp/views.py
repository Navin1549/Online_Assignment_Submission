from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'myapp/home.html')


def contact(request):
    return render(request,'myapp/contact.html')


def adminpg(request):
    return render(request,'myapp/adminpg.html')

def slogin(request):
    return render(request,'myapp/slogin.html')

def tlogin(request):
    return render(request,'myapp/tlogin.html')

def sreg(request):
    return render(request,'myapp/sreg.html')
# Create your views here.
