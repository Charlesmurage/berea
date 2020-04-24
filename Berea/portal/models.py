from django.db import models

# Create your models here.
class Classroom(models.Model):
    class_name = models.CharField(max_length=200)

    def __str__(self):
        return self.class_name