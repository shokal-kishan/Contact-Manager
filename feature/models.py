from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.name

