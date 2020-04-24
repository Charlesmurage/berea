from django.contrib import admin
from .models import Student, Unit

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Student)

class UnitAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Unit)

