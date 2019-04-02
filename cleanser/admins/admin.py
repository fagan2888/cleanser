from django.contrib import admin

from cleanser.core.models import Concept, Document, Object, Project



for m in [Concept, Document, Object, Project]:
  admin.site.register(m)
