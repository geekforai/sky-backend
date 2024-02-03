from django.db import models
from user.models import User
class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    employer_name=models.CharField(max_length=100)
    job_id = models.CharField(max_length=20, unique=True)
    job_role = models.CharField(max_length=100)
    qualification = models.TextField()
    job_title = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    posted_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    link=models.TextField()

