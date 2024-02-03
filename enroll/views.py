# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from enroll.models import Enroll
from enroll.serializer import EnrollSerializer
from rest_framework.permissions import IsAuthenticated
from user.renderers import CostumRender
class EnrollListView(APIView):
    permission_classes=[IsAuthenticated]
    renderer_classes=[CostumRender]
    def post(self, request, *args, **kwargs):
        user = request.user  # Assuming user is authenticated
        course_id = request.data.get('course_id')  # Assuming you send course_id in the request data

        # Check if the user is already enrolled in the course
        if Enroll.objects.filter(user=user, course_id=course_id).exists():
            return Response({'detail': 'User is already enrolled in this course.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new enrollment
        serializer = EnrollSerializer(data={'user': user.id, 'course': course_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
