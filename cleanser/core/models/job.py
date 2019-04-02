# from django.db import models
#
#
# class Job(models.Model):
#   type = models.CharField()
#   priority = models.PositiveSmallIntegerField()
#
#
#
# class Task(models.Model):
#   job = models.ForeignKey(Job, null=True, blank=True, on_delete=models.CASCADE)
#
#   class Meta:
#     abstract = True