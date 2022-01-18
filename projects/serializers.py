from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, HyperlinkedRelatedField
from generic_relations.relations import GenericRelatedField

from .models import *

class FileSerializer(ModelSerializer):
    pass

class ProjectTreeSerializer(ModelSerializer):
    content_object = GenericRelatedField({
        File: FileSerializer,
        Folder: FolderSerializer,
        Play: HyperlinkedRelatedField(
            queryset=Play.objects.all(),
            view_name = 'play-detail'
        )
    })
    class Meta:
        model = ProjectTree
        fields = ('content_type', 'object_id', 'content_object', 'parent')


class ProjectSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    name = CharField()
    tree = ProjectTreeSerializer()

    class Meta:
        model = Project
        fields = ('user', 'name','tree')


