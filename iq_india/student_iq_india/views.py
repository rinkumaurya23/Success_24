from django.shortcuts import render,HttpResponse


def home(request):
    return render(request,'home.html')

    

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')