from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def HomePage(request):
    return render (request,'home.html')

def RegisterPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("password not confirmed")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('userlogin')
    
    return render (request,'Register.html')

def LoginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pass1=request.POST.get('pass')
        user=authenticate(request,email=email,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("email or password is incorrect!")
    return render (request,'userlogin.html')

