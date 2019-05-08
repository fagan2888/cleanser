from rest_framework import serializers

from cleanser.core.models.image import Image



class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = (
      'id',
      'file',
      'source_url',
      'source_id'
    )