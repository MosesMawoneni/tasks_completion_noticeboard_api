from django.db import models
from django.contrib.auth.models import  AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    date_engaged = models.DateField("Date Started Working")
    date_of_birth = models.DateField("Date Of Birth")
    role =  models.CharField(max_length=255)

    def __str__(self):
        return self.name

