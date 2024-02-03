from rest_framework.decorators import APIView
from  rest_framework.response import Response
from jobs.models import Job
from rest_framework import status
from jobs.serializer import JobSerializer
from jobs.renderer import CostumRender
from rest_framework.permissions import IsAuthenticated

class ManageJob(APIView):
    renderer_classes =[CostumRender]
    permission_classes=[IsAuthenticated]
    def get(self,request,id=None):
        if id!=None:
            try:
                data=Job.objects.filter(employer_id=id)
            except Exception as e:
                print(e)
                return Response({
                    'errors':'job not found',
                },status=status.HTTP_404_NOT_FOUND)
            serializeData=JobSerializer(data,many=True)
        else:
            data=Job.objects.all()
            serializeData=JobSerializer(data,many=True)
        return Response({
            'data':serializeData.data
        },status=status.HTTP_200_OK)
    def post(self,request):
        serializer=JobSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Job added successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_501_NOT_IMPLEMENTED)
    def delete(self,request,id):
        obj=Job.objects.get(id=id)
        obj.delete()
        return Response({
            'message':'deleted'
            },status=status.HTTP_200_OK)
