from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

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
        return self.firstname

class Unit(models.Model):
    unit_name = models.CharField(max_length= 60)
    unit_code = models.CharField(max_length=60)
    tutor_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_createdby', on_delete=models.CASCADE)
    tutor_contact = models.CharField(max_length=10)


    def __str__(self):
        return self.unit_name

        
class Classroom(models.Model):
    class_name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, through='Membership')
    units = models.ForeignKey(Unit ,on_delete=models.CASCADE, null= True, blank= True )

    def __str__(self):
        return self.class_name


class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.student




	
	
	
	