# from django.db import models
# from django.contrib.postgres import fields
#
#
# class Source(models.Model):
#   name = models.CharField()
#
#
# class Reference(models.Model):
#   source = models.ForeignKey(Source, on_delete=models.CASCADE)
#   uri = models.URLField(blank=True, null=True)
#   identifier = models.CharField(max_length=64, blank=True, null=True)
#   data = fields.JSONField(default=dict, null=True, blank=True)
#
#   class Meta:
#     abstract = True
#
#
# class ImageReference(Reference):
#   image = models.ForeignKey(
#     'core.Image',
#     on_delete=models.CASCADE,
#     related_name='reference'
#   )
#
