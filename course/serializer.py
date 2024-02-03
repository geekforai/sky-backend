from rest_framework import serializers
from course.models import Course

class CourseSeializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
    def create(self, validated_data):
        course=Course.objects.create(**validated_data)
        course.save()
        return course
class CourseGetSeializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        
        
        