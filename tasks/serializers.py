from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','worker','task_name','task_description','complete','other_explanation')