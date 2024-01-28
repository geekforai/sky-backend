from django.db import IntegrityError
from rest_framework.decorators import APIView
from recruiter.models import Employer,Job
from recruiter.Seializer import EmployeeSerializer,JobSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework import status
class ManageEmployer(APIView):
    def get(self,request,id=None):
        if id!=None:
            data=Employer.objects.get(id=id)
            serializeData=EmployeeSerializer(data)
        else:
            data=Employer.objects.all()
            serializeData=EmployeeSerializer(data,many=True)
        return Response({
            'status':200,
            'data':serializeData.data
        })
    def delete(self,request,id):
        obj=Employer.objects.get(id=id)
        obj.delete()
        return Response({
            'status':200,
            'message':'deleted'
            })
    def post(self,request):
        company_name=request.POST.get('company_name')
        contact_person=request.POST.get('contact_person')
        username=request.POST.get('email')
        password=request.POST.get('password')
        if company_name==None:
            try:
                print(username)
                print(password)
                logindata =Employer.objects.get(username=username,password=password)
                print(EmployeeSerializer(logindata).data)
                return Response({
                    'status':200,
                    'data':EmployeeSerializer(logindata).data,
                })
            except Exception as e:
                print(e)
                pass
        else:
            print('else')
        try:
            data=Employer(company_name=company_name,contact_person=contact_person,
                      username=username,password=password)
            refresh = RefreshToken.for_user(data)
            data.save()
            return Response({
                'status':200,
                'username':contact_person,
                'token':str(refresh.access_token)
            })
        except IntegrityError as e:
            print(e)
            return Response({
                'status':403,
                'message':str(e)
            })
        except:
        # Process the data and perform necessary actions
            return Response({'message':str(e)}, status=status.HTTP_201_CREATED)
class ManageJob(APIView):
    def get(self,request,id=None):
        if id!=None:
            try:
                data=Job.objects.filter(employer_id=id)
            except Exception as e:
                print(e)
                return Response({
                    'mesaage':'job not found',
                })
            serializeData=JobSerializer(data,many=True)
        else:
            data=Job.objects.all()
            serializeData=JobSerializer(data,many=True)
        return Response({
            'status':200,
            'data':serializeData.data
        })
    def post(self,request):
        job_id=request.POST.get('job_id')
        job_role=request.POST.get('job_role')
        qualification=request.POST.get('qualification')
        job_title=request.POST.get('job_title')
        salary=request.POST.get('salary')
        description=request.POST.get('description')
        requirements=request.POST.get('requirements')
        location=request.POST.get('location')
        posted_date=request.POST.get('posted_date')
        deadline=request.POST.get('deadline')
        link=request.POST.get('link')
        employer_id=request.POST.get('employer_id')
        employer_name=request.POST.get('employer_name')
        data=Job(job_id=job_id,job_role=job_role,qualification=qualification,
                 job_title=job_title,salary=salary,description=description,requirements=requirements,
                 location=location,posted_date=posted_date,deadline=deadline,link=link,employer_id=employer_id,employer_name=employer_name)
        try:
            refresh = RefreshToken.for_user(data)
            data.save()
            return Response({
                'status':200,
                'message':'update_success'
            })
        except IntegrityError as e:
            print(e)
            return Response({
                'status':403,
                'message':str(e)
            })
        except:
        # Process the data and perform necessary actions
            return Response({'message':str(e)}, status=status.HTTP_201_CREATED)
    def delete(self,request,id):
        obj=Job.objects.get(id=id)
        obj.delete()
        return Response({
            'status':200,
            'message':'deleted'
            })

