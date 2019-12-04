from django.db import models
from django.contrib.postgres import fields
import uuid

from .utils import TimeMixin



class Model(TimeMixin, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(blank=True, default='', max_length=64)
  slug = models.SlugField(blank=True, max_length=32, unique=True)

  params = fields.JSONField(
    null=True,
    blank=True,
    default=dict
  )

  meta = fields.JSONField(
    null=True,
    blank=True,
    default=dict
  )

  loaded_checkpoint = None

  project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, blank=True)

  # schema = fields.JSONField(
  #   null=True,
  #   blank=True,
  #   help_text='JSON Schema for `inputs` and `outputs` of the model'
  # )

  class Meta:
    db_table = 'model'

