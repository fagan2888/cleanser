from django.db import models
import uuid

from .utils import TimeMixin, OwnedMixin


class Project(OwnedMixin, TimeMixin, models.Model):
  # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  slug = models.SlugField(
    max_length=32,
    unique=True,
    blank=True,
    null=True
  )

  name = models.CharField(
    max_length=32
  )

  class Meta:
    db_table = 'project'
