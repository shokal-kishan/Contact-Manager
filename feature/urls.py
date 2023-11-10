
from django.contrib import admin
from django.urls import path,include
from feature import views 
app_name="feature"
urlpatterns = [
    path('feature/',views.index,name="index"),
    path('add/',views.add,name="add"),
    path('feature/delete/<int:phone>',views.delete,name="delete"),
]

