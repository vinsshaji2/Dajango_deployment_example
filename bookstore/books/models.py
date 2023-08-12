from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class UserLogin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.email


class FormRegister(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    DOB = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=500)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    metrials = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.email
