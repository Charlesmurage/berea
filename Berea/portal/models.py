from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    seccondname = models.CharField(max_length=30)
    studentID = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    nationality = models.CharField(max_length=30)
    phoneNo = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatar', blank=True)


    def __str__(self):
        return self.studentID

class Unit(models.Model):
    unit_name = models.CharField(max_length= 60)
    unit_code = models.CharField(max_length=60)
    tutor_name = models.CharField(max_length=60)
    tutor_contact = models.CharField(max_length=60)


    def __str__(self):
        return self.unit_name

        



	
	
	
	