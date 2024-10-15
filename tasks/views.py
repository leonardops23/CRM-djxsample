from django.views.generic import View
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Tasks


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()
