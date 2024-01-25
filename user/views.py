from typing import Any
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from user.models import User,Education,Skill,Experience
from user.user_serializer import Userserializer,EducationSerializer,ExperienceSerializer,SkillSerializer
from django.db.utils import IntegrityError
from rest_framework import status
from django.core import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserManage(APIView):
    def get(self, request, id=None, *args, **kwargs):
        try:
            if(id==None):
                users=User.objects.all()
                userserializer=Userserializer(users,many=True)
            else:
                users=User.objects.get(id=id)
                userserializer=Userserializer(users)
            return Response({
                'status':'200',
                'data':userserializer.data
            })
        except Exception as e:
            print(e)
            return Response({"message": "This is a GET request"}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Handle POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data=User(first_name=first_name,last_name=last_name,username=email,password=password)
        if first_name==None:
            try:
                logindata =User.objects.get(username=email,password=password)
                print(Userserializer(logindata).data)
                return Response({
                    'status':200,
                    'data':Userserializer(logindata).data,
                })
            except Exception as e:
                print(e)
                pass
        else:
            print('else')
        try:
            data.save()
            refresh = RefreshToken.for_user(data)
            return Response({
                  'status':403,
                'message':'Registered Success',
                'username':f'{first_name} {last_name}',
                'access':str(refresh),
                'token':str(refresh.access_token),
            })
        except IntegrityError as e:
            print(e)
            return Response({
                'status':403,
                'message':'dulicate_entry'
            })
        except:
        # Process the data and perform necessary actions
            return Response({"message": "This is a POST request"}, status=status.HTTP_201_CREATED)

    def put(self, request,id, *args, **kwargs):
        print(id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user=get_object_or_404(User,id=id)
        except Exception as e:
            print(e)

        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.password=password
        user.save()
        # Process the data and perform necessary actions
        return Response({"message": "Updated Success"}, status=status.HTTP_200_OK)

    def delete(self, request,id, *args, **kwargs):
        user=get_object_or_404(User,id=id)
        user.delete()
        # Handle DELETE request
        # Perform necessary actions for deleting resources
        return Response({"message": "Deleted Success"}, status=status.HTTP_204_NO_CONTENT)





#Education Management
class EducationManage(APIView):
    def get(self,request,id=None):
        if(id!=None):
            data=Education.objects.get(user_id=id)
            serialzeData=EducationSerializer(data)
        else:
            data=Education.objects.all()
            serialzeData=EducationSerializer(data,many=True)
        return Response({
            'status':'200',
            'message':'ok',
            'data':serialzeData.data
        })
    def post(self,request):
        user_id=request.POST.get('user_id')
        print(user_id)
        institution_name=request.POST.get('institution_name')
        print(institution_name)
        degree=request.POST.get('degree')
        field_of_study=request.POST.get('field_of_study')
        graduation_date=request.POST.get('graduation_date')
        gpa=request.POST.get('gpa')
        educationData=Education(institution_name=institution_name,degree=degree,field_of_study=field_of_study,graduation_date=graduation_date,gpa=gpa,user_id=user_id)
        try:
            educationData.save()
            return Response({
                'status':200,
                'message':'ok',
            })
        except IntegrityError as e:
            print(e)
            return Response({
                'status':'403',
                'message':'duplicate_entry'
            })
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_403_FORBIDDEN)
    def put(self,request,id):
        data=get_object_or_404(Education,id=id)
        institution_name=request.POST.get('institution_name')
        degree=request.POST.get('degree')
        field_of_study=request.POST.get('field_of_study')
        graduation_date=request.POST.get('graduation_date')
        gpa=request.POST.get('gpa')
        data.institution_name=institution_name
        data.degree=degree
        data.field_of_study=field_of_study
        data.graduation_date=graduation_date
        data.gpa=gpa
        data.save()
        return Response({
            'stutus':200,
            'message':'Update Success'
        })
    def delete(self,request,id):
        data=get_object_or_404(Education,id=id)
        data.delete()
        return Response({
            'status':200,
            'message':'Delete Success'
        })


#Manage Experiance
class ManageExperiance(APIView):
    def get(self,request,id=None):
        if(id!=None):
            data=Experience.objects.get(user_id=id)
            experienceSerializer=ExperienceSerializer(data)
        else:
            data=Experience.objects.all()
            experienceSerializer=ExperienceSerializer(data,many=True)
        return Response({
            'status':200,
            'data':experienceSerializer.data
        })
    def post(self,request):
        user_id=request.POST.get('user_id')
        job_title=request.POST.get('job_title')
        company_name=request.POST.get('company_name')
        location=request.POST.get('location')
        employment_type=request.POST.get('employment_type')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        responsibilities=request.POST.get('responsibilities')
        achievements=request.POST.get('achievements')
        data=Experience(job_title=job_title,company_name=company_name,
                        location=location,employment_type=employment_type,
                        start_date=start_date,end_date=end_date,responsibilities=responsibilities,
                        achievements=achievements,user_id=user_id)
        try:
            data.save()
            return Response({
                'status':200,
                'message':'Success'
            })
        except IntegrityError as e:
            print(e)
            return Response({
                'status':403,
                'message':'duplicate_entry'
            })
        except:
            return Response({
                'status':'403'
            },status=status.HTTP_409_CONFLICT)
    def put(self,request,id):
        job_title=request.POST.get('job_title')
        company_name=request.POST.get('company_name')
        location=request.POST.get('location')
        employment_type=request.POST.get('employment_type')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        responsibilities=request.POST.get('responsibilities')
        achievements=request.POST.get('achievements')
        data=get_object_or_404(Experience,id=id)
        data.job_title=job_title
        data.company_name=company_name
        data.location=location
        data.employment_type=employment_type
        data.start_date=start_date
        data.end_date=end_date
        data.responsibilities=responsibilities
        data.achievements=achievements
        try:
            data.save()
            return Response({
                'status':200,
                'message':'Success'
            })
        except IntegrityError as e:
            return Response({
                'status':403,
                'message':'duplicate_entry'
            })
        except:
            return Response({
                'status':'403'
            },status=status.HTTP_409_CONFLICT)
    def delete(self,request,id):
        data=get_object_or_404(Experience,id=id)
        data.delete()
        return Response({
            'status':200,
            'message':'Success'
        })
class ManageSkills(APIView):
    def get(self,request,id=None):
        if(id!=None):
            data=Skill.objects.get(user_id=id)
            skilserialzer=SkillSerializer(data)
        else:
            data=Skill.objects.all()
            skilserialzer=SkillSerializer(data,many=True)
        return Response({
            'status':200,
            'data':skilserialzer.data
        })
    def post(self,request):
        user_id=request.POST.get('user_id')
        skill_name=request.POST.get('skill_name')
        proficiency_level=request.POST.get('proficiency_level')
        years_of_experience=request.POST.get('years_of_experience')
        certifications=request.POST.get('certifications')
        data=Skill(skill_name=skill_name,proficiency_level=proficiency_level,
                   years_of_experience=years_of_experience,certifications=certifications,
                   user_id=user_id)
        try:
            data.save()
            return Response({
                'status':200,
                'message':'Success'
            })
        except IntegrityError as e:
            return Response({
                'status':403,
                'message':'duplicate_entry'
            })
        except:
            return Response({
                'status':'403'
            },status=status.HTTP_409_CONFLICT)
    def put(self,request,id):
        skill_name=request.POST.get('skill_name')
        proficiency_level=request.POST.get('proficiency_level')
        years_of_experience=request.POST.get('years_of_experience')
        certifications=request.POST.get('certifications')
        data=get_object_or_404(Skill,id=id)
        data.skill_name=skill_name
        data.proficiency_level=proficiency_level
        data.years_of_experience=years_of_experience
        data.certifications=certifications
        try:
            data.save()
            return Response({
                'status':200,
                'message':'Success'
            })
        except IntegrityError as e:
            return Response({
                'status':403,
                'message':'duplicate_entry'
            })
        except:
            return Response({
                'status':'403'
            },status=status.HTTP_409_CONFLICT)
    def delete(self,request,id):
        data=get_object_or_404(Skill,id=id)
        data.delete()
        return Response({
            'status':200,
            'message':'Success'
        })




        
