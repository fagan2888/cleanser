



from django.db import models
from django.contrib.postgres import fields
import uuid

from .utils import TimeMixin
from .model import Model
from .image import Image
from ..querysets.embeddings import EmbeddingQuerySet


# class Embedding(models.Model):
#   model = models.ForeignKey(
#     Model,
#     on_delete=models.CASCADE,
#     related_name='embeddings'
#   )
#   vector = fields.ArrayField(models.FloatField())


class ImageEmbedding(models.Model):
  model = models.ForeignKey(
    Model,
    on_delete=models.CASCADE,
    related_name='image_embeddings'
  )
  image = models.ForeignKey(
    Image,
    on_delete=models.CASCADE,
    related_name='embeddings'
  )
  vector = fields.ArrayField(models.FloatField())

  objects = EmbeddingQuerySet.as_manager()