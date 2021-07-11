from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.shortcuts import redirect
from .models import BlockBuster
def index(request):
    products=BlockBuster.objects.all()
    return render(request,'index.html',{'products':products})
def profile(request):
    return render(request,'profile.html')

def handleSignUp(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if User.objects.filter(username=username).exists():
            messages.error(request, " User name taken. Try using another one")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Your AlcherStream account has been successfully created")
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse("404 - Not found")

def handleSignIn(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponse("404- Not found")

    
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
