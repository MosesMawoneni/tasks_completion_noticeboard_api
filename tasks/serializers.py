from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','worker','task_name','task_description','complete','other_explanation')


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id",
                  "date_engaged",
                  "role")