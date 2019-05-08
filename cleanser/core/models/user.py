import uuid

from django.core.mail import send_mail
from django.db import models


from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
  UserManager
from django.utils import timezone

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    """Allow an empty string or a 3-32 character long string"""
    regex = r'(^$|^[\w._]{3,32}$)'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, _ and . characters and be between 3 and 32 characters'
    )
    flags = 0



class UserManagerWithOptionalUsername(UserManager):
  def _create_user(self, username, email, password, **extra_fields):
    """
    Create and save a user with the given username, email, and password.
    """
    # NOTE: Just commented these lines from the original implementation to
    # allow null user-names
    # if not username:
    #   raise ValueError('The given username must be set')
    email = self.normalize_email(email)
    username = self.model.normalize_username(username)
    user = self.model(username=username, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, username=None, email=None, password=None,
                  **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
  """
  A slightly modified User model that:
  - replaces autoincrement id with UUID
  - makes username optional
    - restricts username to 3-32 characters, numbers, . or _
  - replaces first_name and last_name fields with name
  """
  # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  # replace first and last name with just name for full name
  name = models.CharField(_('full name'), max_length=128, blank=True)

  # Force email to be unique
  email = models.EmailField(_('email address'), blank=True, unique=True, null=True)

  username_validator = UsernameValidator()

  # Make username optional, but unique if one is selected
  username = models.CharField(
    _('username'),
    max_length=32,
    null=True,
    blank=True,
    unique=True,
    help_text=_(
      '3-32 characters. Letters, digits _ or . only.'),
    validators=[username_validator],
    error_messages={
      'unique': _("A user with that username already exists."),
    },
  )

  is_staff = models.BooleanField(
    _('staff status'),
    default=False,
    help_text=_('Designates whether the user can log into this admin site.'),
  )
  is_active = models.BooleanField(
    _('active'),
    default=True,
    help_text=_(
      'Designates whether this user should be treated as active. '
      'Unselect this instead of deleting accounts.'
    ),
  )

  meta = JSONField(default=dict, blank=True, help_text='Extra data about the user')

  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

  objects = UserManagerWithOptionalUsername()

  EMAIL_FIELD = 'email'

  # by default this is `username` in standard django user model
  USERNAME_FIELD = 'username'

  # this is only used by createsuperuser command
  # https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
  REQUIRED_FIELDS = ['email']

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')
    db_table = 'user'

  def clean(self):
    super().clean()
    self.email = self.__class__.objects.normalize_email(self.email)

  def get_full_name(self):
    return self.name

  def get_short_name(self):
    """Return the short name for the user."""
    return self.name

  def email_user(self, subject, message, from_email=None, **kwargs):
    """Send an email to this user."""
    send_mail(subject, message, from_email, [self.email], **kwargs)

  def __str__(self):
    if self.username: return self.username
    if self.email: return self.email
    return str(self.id)