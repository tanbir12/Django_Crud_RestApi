from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=5)
    mobile = models.IntegerField()


    