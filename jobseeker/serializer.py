from rest_framework import serializers
from jobseeker.models import Skill,Education,Experience

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'
class EducationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'
    def validate(self, attrs):
        id=self.context.get('id')
        if Education.objects.filter(id=id).exists():
            education_instance=Education.objects.get(id=id)
            for key ,value in attrs.items():
                setattr(education_instance,key,value)
            education_instance.save()
            return attrs
        else:
            raise serializers.ValidationError('Data not found')
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'
                      
class SkillUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'
    def validate(self, attrs):
        id=self.context.get('id')
        if Skill.objects.filter(id=id).exists():
            skill_instance=Skill.objects.get(id=id)
            for key ,value in attrs.items():
                setattr(skill_instance,key,value)
            skill_instance.save()
            return attrs
        else:
            raise serializers.ValidationError('Data not found')
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields='__all__'
class ExperienceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields='__all__'
    def validate(self, attrs):
        id=self.context.get('id')
        if Experience.objects.filter(id=id).exists():
            experience_instance=Skill.objects.get(id=id)
            for key ,value in attrs.items():
                setattr(experience_instance,key,value)
            experience_instance.save()
            return attrs
        else:
            raise serializers.ValidationError('Data not found')


        
