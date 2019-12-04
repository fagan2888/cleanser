from django.contrib import admin

from cleanser.core.models import (
  Concept,
  # Document,
  # Object,
  Project,
  Image,
  ImageAnnotation,
  Model,
  ImageEmbedding,

  Experiment,
  Run,
  Checkpoint,
  Event,

  Dataset,
  Account
)



for m in [
  # Image,
  ImageAnnotation,
  ImageEmbedding
]:
  admin.site.register(m)


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'slug', 'time_created', 'time_modified')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
  list_display = ('id', 'time_created', 'time_modified')


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'time_created', 'time_modified')


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'root', 'project_id', 'time_created', 'time_modified')


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'root', 'time_started', 'time_completed', 'time_created', 'time_modified')


@admin.register(Checkpoint)
class CheckpointAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'time_created', 'time_modified')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display = ('id', 'time_created', 'time_modified')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'time_created', 'time_modified')


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'project_id', 'time_created', 'time_modified')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'time_created', 'time_modified')