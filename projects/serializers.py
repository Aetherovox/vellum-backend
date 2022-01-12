from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField
from .models import Project


class ComponentSerializer(ModelSerializer):
    project = PrimaryKeyRelatedField(read_only=True)


class ProjectSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    name = CharField()

    class Meta:
        model = Project
        fields = ('user', 'name',)



