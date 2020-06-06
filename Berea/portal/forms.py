from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Student, Tutor, User
from django.db import transaction


class StudentSignUp(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    student_id = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.object.create(user=user)
        Student.student_id = self.cleaned_data.get('student_id')
        Student.email = self.cleaned_data.get('email')
        student.save()
        return student



class TutorSignUp(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    tutor_id = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        tutor = Tutor.object.create(user=user)
        Tutor.tutor_id = self.cleaned_data.get('tutor_id')
        Tutor.email = self.cleaned_data.get('email')
        tutor.save()
        return tutor
    
    
