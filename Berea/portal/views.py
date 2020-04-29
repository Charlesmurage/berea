from django.shortcuts import render,redirect
from .forms import StudentSignUp
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Classroom
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ClassRoomForm

# Create your views here.
@login_required
def home(request):

    return render(request, 'tutorhome.html')


def signup(request):
    if request.method == 'POST':
        form = StudentSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    else:
        form = StudentSignUp()
    return render (request, 'portal/signup.html', {'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup_view.html', {'form': form})

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
    
    print(classes)
    return render(request,'classes.html',{'classes':classes})