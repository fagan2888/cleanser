from rest_framework.viewsets import ModelViewSet


from ..serializers.concept import ConceptSerializer, Concept


class ConceptViewSet(ModelViewSet):
  queryset = Concept.objects.all()
  serializer_class = ConceptSerializer

  lookup_field = 'pk'
  lookup_value_regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'


class SlugBasedConceptViewSet(ModelViewSet):
  queryset = Concept.objects.all()
  serializer_class = ConceptSerializer

  lookup_field = 'slug'