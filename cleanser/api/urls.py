

from rest_framework.routers import DefaultRouter
from django.urls import path, include


from .views.image import ImageViewSet
from .views.annotation import ImageAnnotationViewSet
from .views.concept import ConceptViewSet, SlugBasedConceptViewSet

router = DefaultRouter()
router.register('images', ImageViewSet)

router.register('concepts', ConceptViewSet)  # UUIDs
router.register('concepts', SlugBasedConceptViewSet)  # slugs

router.register('annotations/images', ImageAnnotationViewSet)


urlpatterns = [
  path('', include(router.urls)),
]