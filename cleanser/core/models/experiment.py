from django.conf import settings
from django.db import models
from django.contrib.postgres import fields
import uuid

from .utils import TimeMixin


PROJECTS_ROOT = settings.CLEANSER_ROOT / 'projects'
EXPERIMENTS_ROOT = settings.CLEANSER_ROOT / 'experiments'
"""
TODO:
  - dataset
  - metrics
  - files / artifacts
  - logs

"""


class Experiment(TimeMixin, models.Model):
  name = models.CharField(blank=True, default='', max_length=64)
  slug = models.SlugField(blank=True, max_length=32, null=True)

  description = models.TextField(blank=True)

  meta = fields.JSONField(null=True, blank=True, default=dict)

  project = models.ForeignKey(
    'Project',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name='experiments'
  )
  parent = models.ForeignKey(
    'Experiment', null=True, blank=True, on_delete=models.DO_NOTHING
  )

  class Meta:
    db_table = 'experiment'

  def run(self, **kwargs):
    """Create a new training run"""
    return Run(experiment=self, **kwargs)

  @property
  def root(self):
    if self.project_id:
      return self.project.root / 'experiments' / str(self.id)
    return EXPERIMENTS_ROOT / str(self.id)

  def __repr__(self):
    return f"<Experiment: {self.slug or self.name} ({self.id})>"


class Run(TimeMixin, models.Model):
  name = models.CharField(blank=True, default='', max_length=64)
  slug = models.SlugField(blank=True, max_length=32, null=True)

  time_started = models.DateTimeField(null=True, blank=True, default=None)
  time_completed = models.DateTimeField(null=True, blank=True, default=None)

  params = fields.JSONField(null=True, blank=True, default=dict)

  meta = fields.JSONField(null=True, blank=True, default=dict)

  experiment = models.ForeignKey(
    Experiment, on_delete=models.CASCADE, null=True, blank=True
  )
  # model = models.ForeignKey('core.Model', on_delete=models.CASCADE, null=True, blank=True)
  initial_checkpoint = models.ForeignKey(
    'core.Checkpoint',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name='runs_started_with'
  )

  class Meta:
    db_table = 'experiment_run'

  @property
  def root(self):
    return EXPERIMENTS_ROOT / str(self.experiment_id) / 'runs' / str(self.id)

  def event(self):
    pass

  def start(self):
    pass
    # self.time_started = now

  def end(self):
    pass

  def error(self):
    pass

  def __enter__(self):
    self.start()

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.end()

  def compress(self):
    pass


class Event(TimeMixin, models.Model):
  run = models.ForeignKey(
    Run,
    on_delete=models.CASCADE,
    related_name='events',
    blank=False,
    null=False
  )

  step = models.PositiveIntegerField(null=True, blank=True, default=None)
  data = fields.JSONField(null=True, blank=True, default=dict)

  class Meta:
    db_table = 'experiment_run_event'


class Checkpoint(TimeMixin, models.Model):
  name = models.CharField(blank=True, default='', max_length=64)
  slug = models.SlugField(blank=True, max_length=32, null=True)

  step = models.PositiveIntegerField(null=True, blank=True, default=None)

  meta = fields.JSONField(null=True, blank=True, default=dict)

  model = models.ForeignKey(
    'core.Model',
    blank=False,
    null=False,
    related_name='checkpoints',
    on_delete=models.CASCADE
  )
  run = models.ForeignKey(
    'core.Run', on_delete=models.CASCADE, null=True, blank=True
  )

  class Meta:
    db_table = 'checkpoint'
