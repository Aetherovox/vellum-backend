from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_projects')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class ProjectTree(MPTTModel):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')


# TODO: acts, scenes, characters
class Play(Project):
    playwright = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    datetime_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, {self.playwright}'


class Character(models.Model):
    name = models.CharField(max_length=50)
    play = models.ForeignKey(Play,on_delete=models.CASCADE, related_name='characters')
    actor = models.ForeignKey(User,on_delete=models.PROTECT, related_name='roles')

    def __str__(self):
        return f'{self.name}, {self.play}'


class Act(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='acts')
    num = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.play}, {self.num}'


class Scene(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='scenes')
    act = models.ForeignKey(Act, on_delete=models.PROTECT, related_name='scenes')
    num = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.play}, {self.act}, {self.num}'


class Speech(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='speech')
    text = models.TextField()

