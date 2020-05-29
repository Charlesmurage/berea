from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Classroom, Unit, Notes
from django.contrib.auth import login, authenticate
from .models import Classroom, Student
from .forms import ClassRoomForm,StudentSignUp
from .decorators import allowed_users
from django.contrib.auth.models import Group

# Create your views here.

@login_required
def home_view(request):
    return render(request, 'portal/index.html')


def signup_view(request):
    if request.method == 'POST':
        form = StudentSignUp(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            group = Group.objects.get(name='students')
            user.groups.add(group)
            return redirect('login')
    else:
        form = StudentSignUp()
    return render(request, 'portal/signup_view.html', {'form': form})

def new_class(request):
    current_user = request.user
    if request.method =='POST':
        form = ClassRoomForm(request.POST, request.FILES)


        if form.is_valid():
            group = form.save(commit=False)

            group.save()
            return redirect('home')

    else:
        form = ClassRoomForm()
    return render(request, 'new_class.html', {"form":form})

def classes(request):
    print("-" * 30)
    print("Hello")
    classes= Classroom.objects.all()
    return render(request,'classes.html',{'classes':classes})
    

def new_class(request):
    current_user = request.user
    if request.method =='POST':
        form = ClassRoomForm(request.POST, request.FILES)


        if form.is_valid():
            group = form.save(commit=False)

            group.save()
            return redirect('home')

    else:
        form = ClassRoomForm()
    return render(request, 'new_class.html', {"form":form})
@login_required(login_url='/login/')
def classes(request,classroom_id):
    print("-" * 30)
    print("Hello")
    current_user = request.user
    userID= current_user.id
    classes= Classroom.objects.filter(userID ='classroom_id')
    
    print(classes)
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


