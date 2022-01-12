from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_projects')
    name = models.CharField(max_length=50)


class ProjectComponent(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_components')


# TODO: acts, scenes, characters
class Play(Project):
    playwright = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    datetime_published = models.DateTimeField(default=timezone.now)


class Character(models.Model):
    name = models.CharField(max_length=50)
    play = models.ForeignKey(Play,on_delete=models.CASCADE, related_name='characters')
    actor = models.ForeignKey(User,on_delete=models.PROTECT, related_name='roles')


class Act(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='acts')
    num = models.PositiveSmallIntegerField(default=1)


class Scene(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='scenes')
    num = models.PositiveSmallIntegerField(default=1)


class Speech(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='speech')
    text = models.TextField()
