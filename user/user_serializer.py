from user.models import User,Education,Skill,Experience
from rest_framework.serializers import ModelSerializer


class Userserializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class EducationSerializer(ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'
class ExperienceSerializer(ModelSerializer):
    class Meta:
        model=Experience
        fields='__all__'
class SkillSerializer(ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'