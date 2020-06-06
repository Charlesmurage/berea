from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Classroom(models.Model):
    class_name = models.CharField(max_length=200)
    class_id = models.CharField(max_length=20)
    
    def __str__(self):
        return self.class_name





class Unit(models.Model):
    unit_name = models.CharField(max_length= 60)
    unit_code = models.CharField(max_length=60)
    tutor_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_createdby', on_delete=models.CASCADE)
    tutor_contact = models.CharField(max_length=10)
    classroo_id = models.ManyToManyField(Classroom)


    def __str__(self):
        return self.unit_name

class Notes(models.Model):
    note_title = models.FileField(null = True, upload_to='notes')
    unit = models.ForeignKey(Unit, on_delete= models.CASCADE, null = True)  

    def __str__(self):
        return self.note

class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    student_id = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    classroom_id = models.ForeignKey(Classroom , on_delete=models.CASCADE)

class Tutor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    tutor_id = models.CharField(max_length=10)
    email = models.CharField(max_length=20)



	
	
	
	
