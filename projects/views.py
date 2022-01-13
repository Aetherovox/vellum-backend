from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from .serializers import ProjectSerializer
from .models import Project
from django.contrib.auth import get_user_model

User = get_user_model()


# TODO: user can only access their own projects
class ProjectsViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def user_projects(self, request):
        user = request.user
        queryset = Project.objects.filter(user=user.id)
        print(queryset)
        serializer = self.get_serializer(queryset,many=True)

        print('Serializer is valid')
        print(f'Serializer data: {serializer.data}')
        return Response(serializer.data,status=status.HTTP_200_OK)


    @action(detail=False)
    def test_action(self,request):
        return Response({'sup':'yo'},status=status.HTTP_418_IM_A_TEAPOT)







