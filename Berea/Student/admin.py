from django.contrib import admin
from .models import Assignment
# Register your models here.
class AssignmentAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Assignment)