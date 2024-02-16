# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from enroll.models import Enroll
from enroll.serializer import EnrollSerializer
from rest_framework.permissions import IsAuthenticated
from user.renderers import CostumRender
import razorpay
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
    def get(self, request, *args, **kwargs):
        user = request.user  # Assuming user is authenticated
        enrollments = Enroll.objects.filter(user=user)
        serializer = EnrollSerializer(enrollments, many=True)
        return Response(serializer.data)
class CreateOrderAPIView(APIView):
    permission_classes=[IsAuthenticated]
    renderer_classes=[CostumRender]
    def post(self, request):
        # Initialize Razorpay client with your API key and secret
       client = razorpay.Client(auth=('rzp_live_uFrztfv4LkN7Q1', 'OQgPwspwzrU2oUfWM2gP1PxA'))

        # Create an order
       try:
        order_data = {
            'amount': int(request.POST.get('price'))*100,
            'currency': 'INR',
            'receipt': 'IRCE12',  # Unique order ID
            'payment_capture': 1  # Automatically capture the payment
        }

        order_response = client.order.create(data=order_data)

        return Response({
            'order_id': order_response['id'],
            'amount': order_response['amount'],
            'currency': order_response['currency'],
            'receipt': order_response['receipt']
        }, status=status.HTTP_201_CREATED)
       except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

