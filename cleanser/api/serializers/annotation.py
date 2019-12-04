from rest_framework import serializers

from cleanser.core.models.annotation import ImageAnnotation



class ImageAnnotationSerializer(serializers.ModelSerializer):
  class Meta:
    model = ImageAnnotation
    fields = (
      'id',
      # 'image',
      # 'concept',
      'data',

      'source_id',
      'source_type',
      'verification_status',
      'time_created',
      'time_modified',
      'time_verified'
    )