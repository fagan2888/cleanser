# from django.db import models
#
#
# class Job(models.Model):
#   type = models.CharField()
#   name = ''
#   priority = models.PositiveSmallIntegerField()
#
#   instructions = models.TextField(help_text='Markdown formatted instructions', blank=True, default='')
#
#
#
# class Task(models.Model):
#   job = models.ForeignKey(Job, null=True, blank=True, on_delete=models.CASCADE)
#
#   time_created = None
#   time_modified = None
#   time_completed = None
#
#   time_claimed = None  # time when a user started working on it (
#   cancelled = False
#
#   group = ''  # for clustering
#
#   @property
#   def status(self):
#     if self.time_completed:
#       return 'Completed'
#     if self.time_completed is None and self.time_claimed:
#       return 'In Progress'
#     if self.time_claimed is None:
#       return 'Pending'
#     if self.cancelled:
#       return 'Cancelled'
#
#   class Meta:
#     abstract = True
#
#
#
# class VerificationTask:
#   pass
#
#
# class AnnotationTask:
#   pass
#
#
# class AnnotationVerificationTask(VerificationTask):
#   pass
#
#
#
# class ConceptAnnotationTask(AnnotationTask):
#   pass
#
#
# class ConceptVerificationTask(VerificationTask):
#   pass
