from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE, related_name='user_projects')
    name = models.CharField(max_length=50)


class ProjectComponent(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_components')


class Play(Project):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('User',on_delete=models.CASCADE)
    datetime_published = models.DateTimeField(default=timezone.now())
    # TODO: acts, scenes, characters

