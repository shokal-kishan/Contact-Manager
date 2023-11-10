from django.shortcuts import render,HttpResponseRedirect,redirect,reverse,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# Create your views here.
from .models import Contact


def index(request):
    if request.user.is_anonymous:
        return redirect('authn:index')
    # print(User)
    contacts=Contact.objects.filter(user=request.user)
    parms={"contacts":contacts}
    return render(request,'feature/index.html',parms)

def add(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    try:
        print('added')
        contact=Contact.objects.create(user=request.user,name=name,email=email,phone=phone)
        contact.save()
    except :
        print("not added")
        return redirect('features:index')
    return redirect('features:index')

def delete(request,phone):
    Contact.objects.filter(phone=phone).delete()
    return redirect("features:index")

