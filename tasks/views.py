from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth import get_user_model

from .models import Task
from .serializers import TaskSerializer, WorkerSerializer
from .permissions import IsPlannerOrReadOnly,IsWorkerOrReadOnly

# The TaskViewSet class is a viewset that allows CRUD operations on Task objects, with permission
# restrictions, filtering, and searching capabilities.

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsWorkerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ('worker','task_name','complete')
    search_fields = ('task_name','worker')


# The WorkerViewSet class is a viewset that allows CRUD operations on Worker objects, with permissions
# restricted to planners and read-only access for others, and includes filtering and searching
# capabilities.
class WorkerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPlannerOrReadOnly]
    serializer_class = WorkerSerializer
    queryset = get_user_model().objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ["role"]
