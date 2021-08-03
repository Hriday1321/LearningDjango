from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request, "index.html")
    
def login(request):
    user = None
    userName = None
    passw = None
    if request.method=="POST":
        userName=request.POST.get('username')
        passw=request.POST.get('password')
    user = authenticate(username=userName, password=passw)
    print(user)
    if user is not None:
        return redirect('/')
    else:
        return render(request, "login.html")
    return render(request, "login.html")
    
def logoutUser(request):
    logout(request)
    return redirect("/login")
