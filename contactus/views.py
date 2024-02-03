from django.shortcuts import render
from rest_framework.response import Response
from contactus.serializer import ContactUsSerializer
from rest_framework import status
from rest_framework.decorators import APIView
from user.renderers import CostumRender
# Create your views here.
class ContactView(APIView):
    renderer_classes=[CostumRender]
    def post(self,request):
        serializer=ContactUsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'success'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_503_SERVICE_UNAVAILABLE)



