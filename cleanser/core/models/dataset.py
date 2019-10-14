
from django.db import models


from .image import Image


class Dataset(models.Model):
  name = models.CharField(max_length=128, unique=True)

  # split = models.CharField()
  # type = models.CharField()  # image, seq2seq, etc

  # short_description = models.CharField()
  # description = models.TextField()

  images = models.ManyToManyField(
    Image,
    through='DatasetImage',
    through_fields=('dataset', 'image')
  )


class DatasetImage(models.Model):
  dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)

  # split = models.CharField(choices=[])




class ImageDataset(Dataset):
  class Meta:
    proxy = True


  @classmethod
  def from_folders(cls, name: str, root: str) -> 'ImageDataset':
    pass
