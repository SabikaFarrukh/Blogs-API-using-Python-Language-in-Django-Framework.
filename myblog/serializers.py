from rest_framework import serializers
from .models import Question, Choice



class Questionserializers (serializers.ModelSerializer):

    class Meta:
        model=Question
        fields='__all__'
    
     
