from django.db.models import QuerySet
from django.core.files import File
from django.core.files.base import ContentFile
from typing import Union, List
import glob


class ImageQuerySet(QuerySet):
  def from_paths(self, paths: Union[str, List[str]], save=True):
    if isinstance(paths, str):
      paths = glob.iglob(paths, recursive=True)
    images = []
    for p in paths:
      img = self.model()
      with open(p, 'rb') as f:
        img.file.save(p.split('/')[-1], f, save=save)
      images.append(img)

    # if save:
    #   self.bulk_create(images)

    return images



