from django.db import models
from django.contrib.postgres import fields as pg_fields
import uuid

from .utils import TimeMixin
from ..utils.decorators import lazy
from ..querysets.image import ImageQuerySet


class Image(TimeMixin, models.Model):
  # TODO: validate that the file is a valid image
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
  file = models.ImageField(upload_to='images/', null=True, blank=True)

  # url

  time_taken = models.DateTimeField(null=True, blank=True)

  # width = models.PositiveSmallIntegerField(null=True, blank=True)
  # height = models.PositiveSmallIntegerField(null=True, blank=True)

  # derived_from = models.ForeignKey('Image', blank=True, null=True,
  #                                  on_delete=models.SET_NULL)

  meta = pg_fields.JSONField(
    default=dict,
    blank=True,
  )


  objects = ImageQuerySet.as_manager()

  class Meta:
    db_table = 'image'


  def annotate(self, concept=None, ):
    raise NotImplementedError()

  @property
  def path(self):
    return self.file.path

  @property
  def is_available(self):
    return self.file

  @lazy
  def pillow(self):
    if not self.file:
      raise ValueError('Image file does not exist')
    from PIL import Image

    return Image.open(self.file)

  @lazy
  def numpy(self):
    import numpy
    return numpy.array(self.pillow)

  @classmethod
  def from_pillow(cls, img):
    pass

  @classmethod
  def from_numpy(cls, array):
    pass

  @classmethod
  def from_url(cls, source_url: str, id=None, validate=True) -> 'Image':
    pass

  @classmethod
  def from_file(cls, path, id=None, validate=True):
    raise NotImplementedError()

  @classmethod
  def validate_file(cls, file):
    raise NotImplementedError()