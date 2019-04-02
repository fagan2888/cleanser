from django.db import models
from django.contrib.postgres import fields
import uuid

from .utils import TimeMixin



class Model(TimeMixin, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  schema = fields.JSONField(
    null=True,
    blank=True,
    help_text='JSON Schema for `inputs` and `outputs` of the model'
  )

  class Meta:
    db_table = 'model'
