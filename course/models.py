from django.db import models
class Course(models.Model):
    corse_title=models.CharField(max_length=255,unique=True)
    course_desc=models.TextField()
    course_img=models.CharField(max_length=255)
    course_duration=models.CharField(max_length=30)
# Create your models here.
