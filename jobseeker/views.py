from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from jobseeker.serializer import EducationSerializer,SkillUpdateSerializer,ExperienceUpdateSerializer,SkillSerializer,ExperienceSerializer,EducationUpdateSerializer
from jobseeker.models import Education,Skill,Experience
from user.renderers import CostumRender
class EducationView(APIView):
    renderer_classes=[CostumRender]
    def post(self,request):
        serializer=EducationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Education added succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id=None):
        if id is not None:
            try:
                data=Education.objects.filter(user_id=id)
                serializer=EducationSerializer(data,many=True)
                return  Response({'data':serializer.data},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'errors':str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            data=Education.objects.all()
            serializer=EducationSerializer(data,many=True)
            return  Response({'data':serializer.data},status=status.HTTP_200_OK)
    def put(self,request,id):
        serializer=EducationUpdateSerializer(data=request.data,context={'id':id})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Education updated succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        if Education.objects.filter(id=id).exists():
            education_instance=Education.objects.get(id=id)
            education_instance.delete()
            return Response({'msg':'Education deleted successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'errors':'Data not found to be delete'},status=status.HTTP_400_BAD_REQUEST)

class SkillView(APIView):
    def post(self,request):
        serializer=SkillSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Education added succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id=None):
        if id is not None:
            try:
                data=Skill.objects.filter(user_id=id)
                serializer=SkillSerializer(data,many=True)
                return  Response({'data':serializer.data},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'errors':str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            data=Skill.objects.all()
            serializer=SkillSerializer(data,many=True)
            return  Response({'data':serializer.data},status=status.HTTP_200_OK)
    def put(self,request,id):
        serializer=SkillUpdateSerializer(data=request.data,context={'id':id})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Education updated succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        if Skill.objects.filter(id=id).exists():
            education_instance=Skill.objects.get(id=id)
            education_instance.delete()
            return Response({'msg':'Education deleted successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'errors':'Data not found to be delete'},status=status.HTTP_400_BAD_REQUEST)
class ExperienceView(APIView):
    def post(self,request):
        serializer=ExperienceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Education added succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id=None):
        if id is not None:
            try:
                data=Experience.objects.filter(user_id=id)
                serializer=ExperienceSerializer(data,many=True)
                return  Response({'data':serializer.data},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'errors':str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            data=Experience.objects.all()
            serializer=ExperienceSerializer(data,many=True)
            return  Response({'data':serializer.data},status=status.HTTP_200_OK)
    def put(self,request,id):
        serializer=ExperienceUpdateSerializer(data=request.data,context={'id':id})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Education updated succesfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        if Skill.objects.filter(id=id).exists():
            education_instance=Skill.objects.get(id=id)
            education_instance.delete()
            return Response({'msg':'Education deleted successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'errors':'Data not found to be delete'},status=status.HTTP_400_BAD_REQUEST)
