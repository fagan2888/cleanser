




from django.conf import settings

if not settings.configured:
  from cleanser.cleanser import settings as cleanser_settings
  settings.configure(**{
    k: v for k, v in cleanser_settings.__dict__.items()
    if k.isupper()
  })

  import django
  django.setup()


from .core.models import (
  Concept,
  Document,
  Object,


  DataImport,
  Dataset,
  Annotation,
Model,
Embedding,
# User,
Project,

)



# def set_default_user(user: User):
#   pass