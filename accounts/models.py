from django.db import models
from django.contrib.auth.models import  AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    date_engaged = models.DateField("Date Started Working",null=True,blank=True)
    date_of_birth = models.DateField("Date Of Birth",null=True,blank=True)
    role =  models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

