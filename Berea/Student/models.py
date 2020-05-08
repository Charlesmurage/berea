from django.db import models

# Create your models here.

class Assignment(models.Model):
    assignment_name = models.CharField(max_length = 60)
    assignment = models.FileField(null = False, upload_to='assignments')
    unit_id = models.CharField(max_length=15)
    comment = models.CharField(max_length=100)