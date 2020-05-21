from django.shortcuts import render
from portal.models import Classroom

# Create your views here.
def Home(request):
    print("-" * 30)
    print("Hello")
    classes= Classroom.objects.all()
    return render (request, 'students/index.html',{'classes':classes})


