from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.decorators import APIView,api_view
from django.contrib.auth import authenticate
from user.serializer import RegisterSerializer,LoginSerilaizer,ResestPasswordSerializer,ChangePasswordSerializer,SendPasswordResetLinkSerializer
from rest_framework import status
from user.models import User
from user.renderers import CostumRender
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegisterView(APIView):
    renderer_classes=[CostumRender]
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user=user)
            response =Response({'msg':'Register Success','token':token,'username':user.name,'userEmail':user.email},status=status.HTTP_201_CREATED)

            return response

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserLoginView(APIView):
    renderer_classes=[CostumRender]
    def post(self,request):
        serialzer=LoginSerilaizer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            email=serialzer.data.get('email')
            password=serialzer.data.get('password')
            usertype=serialzer.data.get('usertype')
            user=authenticate(email=email,password=password,usertype=usertype)
            if user is not None:
                if user.usertype!=usertype:
                    return Response({"msg":"Not Autherized"},status=404)
                user.last_login = timezone.now()
                user.save()
                token=get_tokens_for_user(user=user)
                response =Response({'msg':'Register Success','token':token,'username':user.name,'userEmail':user.email},status=status.HTTP_200_OK)
                # response= Response({'msg':'Login success'},status=status.HTTP_200_OK)
                return response
            else:
                return Response({'msg':'You are not autherized user'},status=status.HTTP_404_NOT_FOUND)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    renderer_classes=[CostumRender]
    def get(self,request):
        request.COOKIES.get('jwt')
        return Response({'msg':'Logout success'},status=status.HTTP_200_OK)
class ChangePasswordView(APIView):
    renderer_classes=[CostumRender]
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=ChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password changed'})
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
class SendPasswordResetLinkView(APIView):
    renderer_classes=[CostumRender]
    def post(self,request):
        serializer=SendPasswordResetLinkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':"Link sent to your registred E-mail to reset password"})
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

        # return Response({})
class ResestPasswordView(APIView):
    def post(self,request,uid,token):
        serializer=ResestPasswordSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return render(request,'thank.html')
        else:
            return HttpResponse(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def get(self, request, uid, token):
        return render(request, 'resetPassword.html')

class GetData(APIView):
    renderer_classes=[CostumRender]
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"msg":'hi'})