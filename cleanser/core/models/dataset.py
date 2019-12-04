
from django.db import models
import uuid
# from .concept import Concept
# from .image import Image
from .utils import TimeMixin, VerificationMixin, SourceMixin


class Dataset(TimeMixin, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  slug = models.SlugField(
    max_length=32,
    unique=True,
    blank=True,
    null=True
  )

  name = models.CharField(
    max_length=32,
    blank=True,
  )

  project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, blank=True)

  class Meta:
    db_table = 'dataset'

  # split = models.CharField()
  # type = models.CharField()  # image, seq2seq, etc

  # short_description = models.CharField()
  # description = models.TextField()

  # images = models.ManyToManyField(
  #   Image,
  #   through='DatasetImage',
  #   through_fields=('dataset', 'image')
  # )
  #
  # concepts = models.ManyToManyField(
  #   Concept,
  #   through='DatasetConcept'
  # )

  def snapshot(self, start_date, end_date, modified=True, limit=None):
    pass
#
#
# class DatasetImage(models.Model):
#   dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
#   image = models.ForeignKey(Image, on_delete=models.CASCADE)
#
#   # split = models.CharField(choices=[])
#
#
# class DatasetConcept(models.Model):
#   dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
#   concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
#
#
# class ImageDataset(Dataset):
#   class Meta:
#     proxy = True
#
#
#   @classmethod
#   def from_folders(cls, name: str, root: str) -> 'ImageDataset':
#     pass
#
#
#   @classmethod
#   def from_lmdb(cls):
#     pass
#
#
#   def to_lmdb(self):
#     pass
#
#
#
# class DatasetSnapshot(models.Model):
#   dataset = models.ForeignKey(Dataset, on_delete=models.SET_NULL)
#
#   start_date = models.DateTimeField()
#   end_date = models.DateTimeField()
#
#   limit = models.PositiveIntegerField()
#
#   name = ''
#   path = ''
#   format = ''
#
#   def get_name(self):
#     pass
#
