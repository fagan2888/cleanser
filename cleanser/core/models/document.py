from django.db import models
from django.contrib.postgres import fields
import uuid

from .utils import TimeMixin


class Document(TimeMixin, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  # type = models.CharField(choices=[])
  data = fields.JSONField()

  hash = models.CharField(max_length=64, blank=True, null=True)

  @property
  def text(self):
    raise NotImplementedError()

  class Meta:
    db_table = 'document'


class TextDocument(Document):
  class Meta:
    proxy = True


class HTMLDocument(Document):
  class Meta:
    proxy = True


class MarkdownDocument(Document):
  class Meta:
    proxy = True


class JSONDocument(Document):
  class Meta:
    proxy = True
