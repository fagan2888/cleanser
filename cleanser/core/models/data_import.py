from django.db import models
from .utils import TimeMixin


class DataImport(models.Model):
  """
  Model to track bulk data imports
  """
  name = models.CharField(max_length=64, blank=True, default='')
  description = models.TextField(blank=True, default='')

  source = models.CharField(max_length=128, blank=True, default='')

  time_created = models.DateTimeField(auto_now_add=True, editable=False)