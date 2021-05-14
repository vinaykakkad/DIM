import json
import pytz
from datetime import datetime, timedelta, date

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# from questions.models import Round


class AccountManager(BaseUserManager):
    def create_user(
        self,
        username,
        email,
        password=None,
        is_active=True,
        staff=False,
        is_superuser=False,
        is_activated=False,
    ):
        if not username:
            raise ValueError("Users must have a unique username.")
        if not email:
            raise ValueError("Users must have an email.")
        if not password:
            raise ValueError("Users must have a password.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            # fullname=fullname
        )

        user.set_password(password)
        user.is_active = is_active
        user.staff = staff
        user.is_superuser = is_superuser
        user.is_activated = is_activated
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, fullname=None, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            # fullname=fullname,
            staff=True,
            is_activated=True,
        )
        return user

    def create_superuser(self, username, email, fullname=None, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
            # fullname=fullname,
            staff=True,
            is_superuser=True,
            is_activated=True,
        )
        return user


ACCOUNT_TYPES = (("recruiter", "recruiter"), ("expert", "expert"), ("user", "user"))


class Account(AbstractBaseUser, PermissionsMixin):
    # custom_fields
    username = models.CharField(unique=True, max_length=220)
    email = models.EmailField()
    fullname = models.CharField(max_length=220, blank=True, null=True)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    # required_fields
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
    ]

    objects = AccountManager()

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.staff

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


# We can add custom methods as per requirements
