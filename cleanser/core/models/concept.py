from django.db import models
from django.contrib.postgres import fields as pg_fields
import uuid

from .utils import TimeMixin, VerificationMixin, SourceMixin
from ..managers.base import DataQuerySet


# class ConceptType(models.Model):
#   # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#   name = models.CharField(max_length=4)
#
#   validate_schema = models.BooleanField(default=True, blank=True)
#   schema = pg_fields.JSONField(
#     blank=True,
#     null=True,
#     help_text='JSON Schema for validating concept props')
#
#   def validate(self, concept):
#     pass
#
#   class Meta:
#     db_table = 'concept_type'


class Concept(VerificationMixin, SourceMixin, TimeMixin, models.Model):
  """
  TODO:
  - part of speech?
  - visually recognizable?
  - translations

  """
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  slug = models.SlugField(blank=True, max_length=32, unique=True)

  name = models.CharField(max_length=64, blank=False)

  description = models.TextField(blank=True, default='')
  # thumbnail = models.ImageField()

  props = pg_fields.JSONField(blank=True, null=True, default=dict)

  meta = pg_fields.JSONField(blank=True, null=True, default=dict)

  # TODO: add weight table to support multiple weights per item
  # weight = models.FloatField(null=True, blank=True, help_text='popularity score')

  # ontology = models.ForeignKey('Ontology', on_delete=models.CASCADE, null=True, blank=True)


  images = models.ManyToManyField(
    'core.Image',
    through='core.ImageAnnotation',
    related_name='concepts'
  )


  objects = DataQuerySet.as_manager()

  class Meta:
    db_table = 'concept'

  def __repr__(self):
    return f'<Concept: "{self.name}" ({self.id})>'

  # @property
  # def abbreviations(self):
  #   pass
  #
  # @property
  # def synonyms(self):
  #   pass
  #
  # @property
  # def common_misspellings(self):
  #   pass
  #
  # def similar_to(self, concept):
  #   pass
  #
  # def same_as(self, concept):
  #   pass
  #
  # def not_same_as(self, concept):
  #   pass
  #
  # def subtype_of(self, concept):
  #   pass
  #
  # def instance_of(self, concept):
  #   pass
  #
  # def special_case_of(self, concept):
  #   pass
  #
  # def variant_of(self, concept):
  #   pass

# class Ontology(TimeMixin, models.Model):  # Taxonomy?
#   name = models.CharField(max_length=64, blank=True)
#   # description = ''
#
#   class Meta:
#     db_table = 'concept'

# class OntologyConcept(models.Model):
#   ontology = ''
#   concept = ''

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
