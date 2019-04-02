from django.db import models
from django.contrib.postgres import fields as pg_fields

from .concept import Concept
from .image import Image
from .utils import TimeMixin
#


class Annotation(TimeMixin, models.Model):
  concept = models.ForeignKey(
    Concept,
    on_delete=models.CASCADE,
    null=True,
    blank=True)

  data = pg_fields.JSONField()
  confidence = models.FloatField(default=None, blank=True, null=True)
  source = models.CharField(max_length=128)

  class Meta:
    abstract = True


class ImageAnnotation(Annotation):
  image = models.ForeignKey(Image, on_delete=models.CASCADE)




class BoundingBox(ImageAnnotation):
  class Meta:
    proxy = True


class Keypoints(ImageAnnotation):
  class Meta:
    proxy = True


class Polygon(ImageAnnotation):
  class Meta:
    proxy = True


class SegmentationMask(ImageAnnotation):
  class Meta:
    proxy = True

