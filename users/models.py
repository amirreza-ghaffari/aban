from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=256, null=True, blank=False)
    last_name = models.CharField(max_length=256, null=True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name + str(self.id)

    @property
    def full_name(self):
        full_name = ''
        if self.last_name:
            full_name = self.last_name
        if self.first_name:
            full_name = self.first_name + ' ' + full_name
        return full_name

    class Meta:
        # Add verbose name
        verbose_name = 'User'


class TomanWallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, primary_key=True)
    balance = models.FloatField(default=100)

    def __str__(self):
        return self.user.email



