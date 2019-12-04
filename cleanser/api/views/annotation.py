from rest_framework.viewsets import ModelViewSet


from ..serializers.annotation import ImageAnnotation, ImageAnnotationSerializer


class ImageAnnotationViewSet(ModelViewSet):
  queryset = ImageAnnotation.objects.all()
  serializer_class = ImageAnnotationSerializer