from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    firstname = models.CharField(_('firstname'), max_length=30)
    lastname = models.CharField(_('lastname'), max_length=30)
    image = models.ImageField(upload_to="user images")
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_prural = _('users')

    def get_full_name(self):
        full_name = f'{self.firstname} {self.lastname}'
        return full_name.strip()

    def get_short_name(self):
        return self.firstname

    def email_user(self, subject, message, from_email, **kwargs):

        send_mail(subject, message, settings.EMAIL_HOST, [self.email], **kwargs)

