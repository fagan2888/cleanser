from django.db import models
from django.contrib.postgres import fields

from ..utils import TimeMixin
from ..experiment import Checkpoint


class Embedding(TimeMixin, models.Model):
  checkpoint = models.ForeignKey(
    Checkpoint,
    on_delete=models.CASCADE,
    related_name='embeddings'
  )

  vector = fields.ArrayField(models.FloatField())

  class Meta:
    abstract = True

