from secrets import choice
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo


class questionlist (APIView):
   def get (self,requests):
       questions1=Question.objects.all()
       serializer=questionserializers(questions1,many=True)
       return response (serializer.data)
   def post (self,requests,format=none):
     choice = [user.choice for user in User.objects.all()]
     return Response(choice)
   
   
   
   