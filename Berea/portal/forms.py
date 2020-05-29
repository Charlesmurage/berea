from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Classroom, Student


class StudentSignUp(UserCreationForm):
    full_name= forms.CharField(required=True)
    email= forms.EmailField()
    
    
    class Meta:
        model = Student
        fields =['full_name','username','email','password1','password2']
        # model = get_user_model()
        # fields =['first_name', 'last_name','username','email','password1','password2'] 

class ClassRoomForm(forms.ModelForm):
    class_name = forms.CharField(max_length=30)

    class Meta:
        model = Classroom
        fields = ['class_name']



class ClassRoomForm(forms.ModelForm):
    class_name = forms.CharField(max_length=30)

    class Meta:
        model = Classroom
        fields = ['class_name']