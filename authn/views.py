from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import get_object_or_404
# Create your views here.
# views.py
# from django.contrib.auth import get_user_model

# User = get_user_model()

def index(request):
    if request.user.is_anonymous:
        return render(request,'authn/login.html')
    return redirect('feature:index')

def usersignup(request):
    return render(request,'authn/signup.html')


def create_user(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        try:
            check=get_object_or_404(User,username=username)
        except:
            try:
                user=User.objects.create_user(username=username,password=password)
                user.save()
            except:
                print("not created")
            return redirect('authn:index')
    
    return redirect('authn:index')
    





def userlogin(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        print(username,password)
        if user is not None:
            login(request,user)
            
        
            return redirect('authns:index')
    
    return redirect('authn:index')


def logoutUser(request):
    logout(request)
    return redirect('authn:index')