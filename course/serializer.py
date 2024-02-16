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
    course_img_data = serializers.SerializerMethodField()
    class Meta:
        model=Course
        fields='__all__'
    def get_course_img_data(self, obj):
        if obj.course_img:
            return obj.course_img.read()
        return None

