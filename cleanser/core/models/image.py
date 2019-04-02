from django.db import models


class Image(models.Model):
  id = models.UUIDField(primary_key=True)

  source_url = models.URLField()
  url = models.URLField()

  width = models.PositiveSmallIntegerField()
  height = models.PositiveSmallIntegerField()

  class Meta:
    db_table = 'image'
