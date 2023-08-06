from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Task

# The TaskSerializer class is a serializer for the Task model with specific fields.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','worker','task_name','task_description','complete','other_explanation')


# The WorkerSerializer class is a serializer for the Worker model, which includes the fields "id",
# "date_engaged", and "role".
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id",
                  "date_engaged",
                  "role")