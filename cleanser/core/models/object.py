from django.db import models
from django.contrib.postgres import fields
import jsonschema

# TODO:
#  - SCHEMA https://github.com/mozilla-services/react-jsonschema-form

class ObjectType(models.Model):
  name = models.CharField(max_length=16, primary_key=True, editable=False)
  schema = fields.JSONField(
    help_text='JSON Schema for validation',
    null=True,
    blank=True
  )


class Object(models.Model):
  type = models.ForeignKey(
    ObjectType,
    on_delete=models.CASCADE,
    null=True,
    blank=True
  )
  data = fields.JSONField()

  class Meta:
    db_table = 'object'

  def validate_schema(self, schema=None):
    schema = schema or (
      self.type.schema
        if self.type and self.type.schema
        else None
    )
    if schema:
      return jsonschema.validate(self.data, schema=schema)
