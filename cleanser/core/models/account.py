from django.db import models
import uuid

from .utils import TimeMixin


class AccountTypeChoices(models.TextChoices):
  PERSONAL = 'person', 'Personal Account'
  ORGANIZATION = 'org', 'Organization'


class Account(TimeMixin, models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  type = models.CharField(
    choices=AccountTypeChoices.choices,
    default=AccountTypeChoices.PERSONAL,
    max_length=8,
    blank=True
  )
  slug = models.SlugField(blank=True, max_length=32, unique=True)
  name = models.CharField(max_length=64, blank=False)
  description = models.TextField(blank=True, default='')

  is_private = models.BooleanField(blank=True, default=False)

  users = models.ManyToManyField('User', through='core.AccountUser')

  class Meta:
    db_table = 'account'


class AccountUser(TimeMixin, models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  user = models.ForeignKey('User', on_delete=models.CASCADE)

  class Meta:
    db_table = 'account_user'