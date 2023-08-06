from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .models import Task
from .serializers import TaskSerializer, WorkerSerializer
from .permissions import IsPlannerOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class WorkerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPlannerOrReadOnly]
    serializer_class = WorkerSerializer
    queryset = get_user_model().objects.all()
