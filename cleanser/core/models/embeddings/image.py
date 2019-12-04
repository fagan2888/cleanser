



from django.db import models

from .base import Embedding
from ..image import Image
from ...querysets.embeddings import EmbeddingQuerySet



class ImageEmbedding(Embedding):
  image = models.ForeignKey(
    Image,
    on_delete=models.CASCADE,
    related_name='embeddings'
  )
  objects = EmbeddingQuerySet.as_manager()

  class Meta:
    db_table = 'image_embedding'