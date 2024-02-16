from django.db import models
class Course(models.Model):
    course_title=models.CharField(max_length=255,unique=True)
    course_desc=models.TextField()
    course_img=models.ImageField(blank=True)
    course_duration=models.CharField(max_length=30)
    price=models.IntegerField()
# Create your models here.
