from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Classroom(models.Model):
    class_name = models.CharField(max_length=200)
    students = models.ManyToManyField( 'Student', related_name = 'Student', through='Membership')
    
    def __str__(self):
        return self.class_name





class Unit(models.Model):
    unit_name = models.CharField(max_length= 60)
    unit_code = models.CharField(max_length=60)
    tutor_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_createdby', on_delete=models.CASCADE)
    tutor_contact = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, on_delete= models.CASCADE, null = True,)


    def __str__(self):
        return self.unit_name

class Notes(models.Model):
    note = models.FileField(null = True, upload_to='notes')
    unit = models.ForeignKey(Unit, on_delete= models.CASCADE, null = True)  

    # def __str__(self):
    #     return self.unit_name      
class Student(AbstractUser):
    full_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE,null=True)



class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.student




	
	
	
	
