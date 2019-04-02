from django.db import models
from django.conf import settings



class TimeMixin:
  time_created = models.DateTimeField(auto_now_add=True, editable=False)
  time_modified = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class OwnedMixin:
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
  )

  class Meta:
    abstract = True


class DeletedFlag:
  time_deleted = models.DateTimeField()
