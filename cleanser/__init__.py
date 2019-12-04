
def configure():
  """
  run django configuration so we can use the module without the standard settings file
  """
  from django.conf import settings
  if not settings.configured:
    from . import settings as cleanser_settings
    settings.configure(**{
      k: v for k, v in cleanser_settings.__dict__.items()
      if k.isupper()
    })

    import django
    django.setup()


configure()

from .core.models import (
  Concept,
  # Document,
  # Object,
  # DataImport,
  # Dataset,
  # ImageDataset,
  # Annotation,
  Model,
  ImageEmbedding,
  # User,
  # Project,
  Image,
  ImageAnnotation,
  Experiment,
  Model,
  Run,
  Event,
  Checkpoint,
  Project,
  Account,
  Dataset
)



# def set_default_user(user: User):
#   pass

import logging

log = logging.getLogger('cleanser')
