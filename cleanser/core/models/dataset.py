
from django.db import models


from .image import Image


class Dataset(models.Model):
  name = models.CharField(max_length=128)

  images = models.ManyToManyField(
    Image,
    through='DatasetImage',
    through_fields=('dataset', 'image')
  )


class DatasetImage(models.Model):
  dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)