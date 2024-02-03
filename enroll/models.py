from django.db import models
from user.models import User
from course.models import Course

class Enroll(models.Model):
    enroll_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    completion_status = models.BooleanField(default=False)
    feedback = models.TextField(blank=True)
    certificate_url = models.URLField(blank=True)
    
    # Add more fields as needed

    def __str__(self):
        return f"Enrollment {self.enroll_id}: {self.user.username} in {self.course.title}"
