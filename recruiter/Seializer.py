from rest_framework import serializers
from recruiter.models import Employer,Job
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields='__all__'
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'