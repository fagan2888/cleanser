from rest_framework import serializers

from cleanser.core.models.concept import Concept



class ConceptSerializer(serializers.ModelSerializer):
  class Meta:
    model = Concept
    fields = (
      'id',
      'name',
      'slug',
      'description',
      'props',
      'meta',

      'time_created',
      'time_modified',

      'verification_status',
      'source_type'
    )