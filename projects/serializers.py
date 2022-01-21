from rest_framework.serializers import (ModelSerializer, PrimaryKeyRelatedField, CharField, HyperlinkedRelatedField
                                        ,StringRelatedField)
from generic_relations.relations import GenericRelatedField

from .models import *


# TODO: Want to serialize based on composition, not inheritance
class FileSerializer(ModelSerializer):
    class Meta:
        fields = ("filename", "encoding", "date_created", "date_updated")


class FolderSerializer(ModelSerializer):
    class Meta:
        fields = ("name", "type")


class ProjectTreeSerializer(ModelSerializer):
    content_type = StringRelatedField()
    content_object = GenericRelatedField({
        File: HyperlinkedRelatedField(
            queryset= File.objects.all(),
            view_name = 'file-detail'
        ),
        Folder: HyperlinkedRelatedField(
            queryset=Folder.objects.all(),
            view_name='folder-detail'
        ),
    })

    class Meta:
        model = ProjectTree
        fields = ('id','content_type', 'object_id', 'content_object', 'parent')


class TreeSerializer(ModelSerializer):

    pass


class ProjectSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    name = CharField()
    tree = ProjectTreeSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id','user', 'name', 'tree')


