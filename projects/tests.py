from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from .models import ProjectTree


class ProjectTreeTests(TestCase):
    def setup(self) -> None:
        # create from serializers
        pass

    def test_content_type_create(self):
        """Creating an object in the tree also creates an object of that type in the datastore"""
        pass

    def test_only_project_types(self):
        """Can only create types from the projects module"""
        try:
            ProjectTree.objects.create(content_type='core.user', object_id=1, content_object=1, parent=None)
        except ObjectDoesNotExist:
            return
        self.assertIsNone(ProjectTree.objects.filter(content_type='core.user'))

