from django.db import models

from ..image import Image
from .base import Annotation


class ImageAnnotation(Annotation):
  schemas = {'bounding_box': '', 'poly': '', 'points': '', 'mask': ''}

  image = models.ForeignKey(
    Image, on_delete=models.CASCADE, related_name='annotations'
  )

  _validate_schema = False

  class Meta:
    db_table = 'image_annotation'

  def __repr__(self):
    return f'<ImageAnnotation: image={self.image_id} concept={self.concept_id} status={self.verification_status}>'

  @property
  def bounding_box(self):
    return self.data.get('bounding_box')

  @bounding_box.setter
  def bounding_box(self, bbox):
    self.data['bounding_box'] = bbox

  @bounding_box.deleter
  def bounding_box(self):
    del self.data['bounding_box']