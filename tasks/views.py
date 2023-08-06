from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model

from .models import Task
from .serializers import TaskSerializer, WorkerSerializer
from .permissions import IsPlannerOrReadOnly,IsWorkerOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsWorkerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('worker','task_name','complete')


class WorkerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPlannerOrReadOnly]
    serializer_class = WorkerSerializer
    queryset = get_user_model().objects.all()
