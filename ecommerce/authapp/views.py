from django.shortcuts import render,redirect

from django.contrib.auth.models import User

# Create your views here.

def handlesignup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirmpassword=request.POST['pass2']

        if password!=confirmpassword:
            #messages.warning(request,"Passwords dint match")
            return render(request,'authapp/signup,html')

        try:
            if User.objects.get(username=email):
                #messages.warning(request,"Email already exists!")
                return render(request,'authapp/signup.html')
        except Exception as identifier:
            pass

        user=User.objects.create_user(email,email,confirmpassword)
        user.save()

    
    return render(request,"signup.html")

def handlelogin(request):
    return render(request,"login.html")

def handlelogout(request):
    return redirect("/authapp/login")

