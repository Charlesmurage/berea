from django.contrib import admin
from .models import Student, Unit, Classroom, Membership, Notes

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Student)

class UnitAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Unit)

class ClassroomAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Classroom)


class MembershipAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Membership)



class NotesAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Notes)
