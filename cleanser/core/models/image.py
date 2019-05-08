from django.db import models
import uuid

from .utils import TimeMixin
from ..utils.decorators import lazy
from ..querysets.image import ImageQuerySet


class Image(TimeMixin, models.Model):
  # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  # TODO: validate that the file is a valid image
  file = models.ImageField(upload_to='images/', null=True, blank=True)

  source_id = models.CharField(max_length=64, blank=True, null=True)
  source_url = models.URLField(
    help_text='url that this image was downloaded from',
    blank=True,
    null=True
  )

  # width = models.PositiveSmallIntegerField(null=True, blank=True)
  # height = models.PositiveSmallIntegerField(null=True, blank=True)

  # derived_from = models.ForeignKey('Image', blank=True, null=True,
  #                                  on_delete=models.SET_NULL)


  objects = ImageQuerySet.as_manager()

  class Meta:
    db_table = 'image'

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