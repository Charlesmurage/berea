from django.contrib import admin
from .models import Student

# Register your models here.
class SrudentAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Student)
