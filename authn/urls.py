from django.contrib import admin 
from django.urls import path
from . import views
app_name='authn'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.userlogin,name='userlogin'),
    path('signup/',views.usersignup,name='usersignup'),
    path('signup/create_user/',views.create_user,name='create_user'),
    path('feature/logout/',views.logoutUser,name='logoutUser')

]