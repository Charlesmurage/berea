from django.shortcuts import render

from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect
from .models import Classroom

from .forms import SignUpForm, ClassRoomForm

# Create your views here.
def signup(request):
    return render (request, 'portal/signup.html')


def home_view(request):
    return render(request, 'home.html')


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