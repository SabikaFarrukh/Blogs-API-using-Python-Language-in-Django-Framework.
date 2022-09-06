from secrets import choice
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Question
from .serializers import Questionserializers


class questionlist (APIView):
  def get (self,request):
    questions1=Question.objects.all()
    serializer=Questionserializers(questions1,many=True)
    return Response (serializer.data)

  def post (self, request, format=None):
    serializer = Questionserializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   
   
   