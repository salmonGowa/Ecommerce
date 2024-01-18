from django.shortcuts import render,redirect

# Create your views here.

def handlesignup(request):
    return render(request,"authentications/signup.html")

def handlelogin(request):
    return render(request,"authentications/login.html")

def handlelogout(request):
    return redirect("/authapp/login")

