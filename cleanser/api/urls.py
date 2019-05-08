

from rest_framework.routers import DefaultRouter
from django.urls import path, include


from .views.image import ImageViewSet

router = DefaultRouter()
router.register('images', ImageViewSet)


urlpatterns = [
  path('', include(router.urls)),
]