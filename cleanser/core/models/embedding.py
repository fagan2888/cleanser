



from django.db import models
from django.contrib.postgres import fields
import uuid

from .utils import TimeMixin
from .model import Model


class Embedding(models.Model):
  model = models.ForeignKey(Model, on_delete=models.CASCADE)
  vector = fields.ArrayField(models.FloatField())
