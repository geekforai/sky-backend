from django.db import models

class Employer(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100)
    username = models.EmailField(unique=True)
    password = models.TextField()

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.job_title
