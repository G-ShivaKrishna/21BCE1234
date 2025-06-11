from rest_framework import serializers
from .models import Task

class TaskSerialzer(serializers.ModelSerializer):
    class Meta:
        Model=Task
        fields='__all__'