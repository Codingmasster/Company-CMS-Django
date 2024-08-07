from django.shortcuts import render,redirect

def base_url(request):
    return render(request,'base.html')

def login_url(request):
    return render(request,'login.html')

def signup_url(request):
    return render(request,'register.html')