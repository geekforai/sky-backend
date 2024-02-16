from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from course.serializer import CourseSeializer,CourseGetSeializer
from course.models import Course
from course.renderer import CostumRender
from rest_framework.permissions import IsAuthenticated
class CourseView(APIView):
    renderer_classes=[CostumRender]
    def post(self,request):
        serializer=CourseGetSeializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Course added successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id=None):
        if id is not None:
            try:
                course = Course.objects.get(id=id)
                serializer = CourseGetSeializer(course)  # Pass the instance, not data
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'errors':str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            courses = Course.objects.all()
            serializer = CourseSeializer(courses, many=True)  # Use many=True for queryset
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    def delete(self,request,id):
            try:
                course = Course.objects.get(id=id)
                course.delete()
                return Response({'msg': "Delete success"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'errors':str(e)},status=status.HTTP_400_BAD_REQUEST)