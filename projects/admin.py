from django.contrib import admin
from .models import Project, ProjectTree, Play

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTree)
admin.site.register(Play)