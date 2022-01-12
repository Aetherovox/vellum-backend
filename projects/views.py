from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer
from .models import Project


# TODO: user can only access their own projects
class ProjectsViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Project.objects.all()
        else:
            return Project.objects.filter(user=user)

