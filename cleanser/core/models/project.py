from django.db import models
from django.conf import settings
import uuid
from django.contrib.postgres import fields as pg_fields

from .utils import TimeMixin, OwnedMixin
from ...utils import shell


class Project(TimeMixin, models.Model):
  id = models.UUIDField(
    primary_key=True, default=uuid.uuid4, editable=False
  )

  slug = models.SlugField(
    max_length=32, blank=True, null=True
  )

  name = models.CharField(
    max_length=32,
    blank=True,
  )

  meta = pg_fields.JSONField(
    default=dict,
    blank=True,
  )

  account = models.ForeignKey(
    'Account', on_delete=models.CASCADE, blank=True, null=True
  )

  is_private = models.BooleanField(default=True, blank=True)

  class Meta:
    db_table = 'project'

  def __repr__(self):
    return (
      f"<Project: "
      f"{self.account.slug if hasattr(self, 'account') and self.account_id else self.account_id}/{self.slug}"
      f" ({self.id})>"
    )

  @property
  def root(self):
    if self.account_id:
      return settings.CLEANSER_ROOT / 'accounts' / str(self.account_id) / 'projects' / str(self.id)
    return settings.CLEANSER_ROOT / 'projects' / str(self.id)

  def experiment(self, **kwargs):
    e, created = self.experiments.get_or_create(
      project_id=self.id, **kwargs
    )
    return e

  @classmethod
  def for_current_git_repo(cls, **kwargs):
    account, repo = shell.github_repo()
    if not repo:
      repo = shell.git_repo_name()
    if not repo:
      raise ValueError(
        "Can't create project for current git "
        "repo because not currently in a git repo"
      )
    project, created = cls.objects.get_or_create(
      slug=repo, name=repo, **kwargs
    )
    return project
