from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField
from .models import Project


class ComponentSerializer(ModelSerializer):
    project = PrimaryKeyRelatedField()


class ProjectSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField()
    name = CharField()
    components = ComponentSerializer()

    class Meta:
        model = Project
        fields = ('user','name',)


