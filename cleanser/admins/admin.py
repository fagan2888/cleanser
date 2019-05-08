from django.contrib import admin

from cleanser.core.models import Concept, Document, Object, Project, Image, Model, ImageEmbedding



for m in [Concept, Document, Object, Project, Image, Model, ImageEmbedding]:
  admin.site.register(m)
