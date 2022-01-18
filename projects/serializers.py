from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField, HyperlinkedRelatedField
from generic_relations.relations import GenericRelatedField

from .models import *

# TODO: Want to serialize based on composition, not inheritance


class FileSerializer(ModelSerializer):

    class Meta:
        fields = ("filename","encoding","date_created","date_updated")
class FolderSerializer(ModelSerializer):
    class Meta:
        fields = ("name","type")


class ProjectTreeSerializer(ModelSerializer):
    content_object = GenericRelatedField({
        File: FileSerializer,
        Folder: FolderSerializer,

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


