from django.db import models
from user.models import User
# Create your models here.
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100, blank=True)
    employment_type = models.CharField(max_length=50, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField(blank=True)
    achievements = models.TextField(blank=True)

    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100,unique=True)
    proficiency_level = models.CharField(max_length=50, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    certifications = models.TextField(blank=True)

    

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=100,unique=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    graduation_date = models.DateField(null=True, blank=True)
    gpa = models.FloatField(null=True, blank=True)