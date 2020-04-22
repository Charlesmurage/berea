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

# class Account(AbstractBaseUser):
#     first_name = models.CharField(max_length=30)
#     seccond_name = models.CharField(max_length=30)
#     student_ID = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     gender = models.CharField(max_length=10)
#     dob = models.DateField()
#     nationality = models.CharField(max_length=30)
#     phoneNo = models.CharField(max_length=30)
#     avatar = models.ImageField(upload_to='avatar', blank=True)
#     date_joined= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login= models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin= models.BooleanField(default=False)
#     is_active= models.BooleanField(default=True)
#     is_staff= models.BooleanField(default=False)
#     is_superuser= models.BooleanField(default=False)

#     USERNAME_FIELD = 'student_ID'
#     REQUIRED_FIELDS = [
#         'first_name',
#         'seccond_name',
#         'email'
#         'student_ID'
#     ]

#     def __str__(self):
#         return self.student_ID + "," + self.first_name

#     # For checking permissions. to keep it simple all admin have ALL permissons
# 	def has_perm(self, perm, obj=None):
#         return self.is_admin
        
		

# 	# # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
# 	# def has_module_perms(self, app_label):
# 	# 	return True
	
	
	
	
	