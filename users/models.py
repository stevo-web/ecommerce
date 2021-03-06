from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    firstname = models.CharField(_('firstname'), max_length=30)
    lastname = models.CharField(_('lastname'), max_length=30)
    image = models.ImageField(upload_to="user images", blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    location = models.CharField(_('location'), max_length=100)
    phone = models.CharField(_('phone'), max_length=20)
    has_shop = models.BooleanField(_('shop'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = f'{self.firstname} {self.lastname}'
        return full_name.strip()

    def get_short_name(self):
        return self.firstname

    def email_user(self, subject, message, from_email, **kwargs):

        send_mail(subject, message, settings.EMAIL_HOST, [self.email], **kwargs)

