# Generated by Django 4.0 on 2022-01-12 10:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_alter_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='roles', to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projects', to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.project')),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('datetime_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('playwright', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
            bases=('projects.project',),
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speech', to='projects.character')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_components', to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField(default=1)),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenes', to='projects.play')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='projects.play'),
        ),
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField(default=1)),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acts', to='projects.play')),
            ],
        ),
    ]