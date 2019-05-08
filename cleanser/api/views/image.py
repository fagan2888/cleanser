from rest_framework.viewsets import ModelViewSet


from ..serializers.image import ImageSerializer, Image


class ImageViewSet(ModelViewSet):
  queryset = Image.objects.all()
  serializer_class = ImageSerializer