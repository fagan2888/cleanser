

from django.db import models
import numpy as np


class EmbeddingQuerySet(models.QuerySet):
  def numpy(self, *extra_fields):
    *extra, vectors = zip(*self.values_list(*extra_fields, 'vector'))
    return (*extra, np.array(vectors))
