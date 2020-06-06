from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Classroom, Unit, Notes
from django.contrib.auth import login, authenticate
from .models import Classroom, Student
from .forms import StudentSignUp
from .decorators import allowed_users
from django.contrib.auth.models import Group

# Create your views here.

@login_required
def home_view(request):
    return render(request, 'portal/index.html')


def signup_view(request):
    return render(request, 'portal/signup.html', {'form': form})
    
@login_required(login_url='/login/')
def classes(request):
    print("-" * 30)
    print("Hello")
    classes= Classroom.objects.all()
    return render(request,'class.html',{'classes':classes})
    
    

@login_required(login_url='/login/')
def units(request,un_id):
    unit = Unit.objects.filter(classroom_id=un_id)
    # print([x.classname for x in classes])
    return render(request,'units.html',{"unit": unit})

@login_required(login_url='/login/')
def notes(request,not_id):
    notes = Notes.objects.filter(unit_id=not_id)
    return render(request,'notes.html',{"notes": notes})


