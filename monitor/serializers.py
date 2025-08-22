from rest_framework import serializers
from .models import Process

#We define a new serializer for our Process model.
class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'
#This converts between Python objects ↔ JSON.