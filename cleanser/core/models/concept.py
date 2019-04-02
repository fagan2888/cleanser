from django.db import models
from django.contrib.postgres import fields as pg_fields
import uuid

from .utils import TimeMixin
from ..managers.base import DataQuerySet

class ConceptType(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=4)

  validate_schema = models.BooleanField(default=True, blank=True)
  schema = pg_fields.JSONField(
    blank=True,
    null=True,
    help_text='JSON Schema for validating concept props')

  def validate(self, concept):
    pass

  class Meta:
    db_table = 'concept_type'


class Concept(TimeMixin, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=64)
  synonyms = pg_fields.ArrayField(models.CharField(max_length=64))

  description = models.TextField()
  # thumbnail = models.ImageField()

  props = pg_fields.JSONField(blank=True, null=True, default=dict)
  # labels = pg_fields.ArrayField(models.CharField())
  #
  # related = models.ManyToManyField(through='Relation')
  # children = models.ManyToManyField(through='Relation')
  # parents = models.ManyToManyField(through='Relation')


  objects = DataQuerySet.as_manager()

  class Meta:
    db_table = 'concept'


# class Relation(TimeMixin, models.Model):
#   head = models.ForeignKey(Concept)
#   tail = models.ForeignKey(Concept)
#   type = models.CharField()
#   value = pg_fields.JSONField()
#
#   class Meta:
#     db_table = 'concept_relation'
#
#
# class RelationType(TimeMixin, models.Model):
#   id = models.CharField(primary_key=True, max_length=6)
#   name = models.CharField()
#
#   class Meta:
#     db_table = 'relation_type'


# class Identifier(TimeMixin, models.Model):
#   concept = models.ForeignKey(Concept, on_delete=models.CASCADE,
#                               related_name='ids')
#   source = models.CharField()
#   value = models.CharField()
#
#   class Meta:
#     db_table = 'concept_identifier'
#     constraints = (
#       models.UniqueConstraint(
#         fields=('source', 'value'),
#         name='unique_source_value'
#       ),
#     )
#
#     indexes = [
#
#     ]
