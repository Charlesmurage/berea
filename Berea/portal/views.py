from django.shortcuts import render,redirect
from .forms import StudentSignUp
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):

    return render(request, 'portal/home.html')

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
