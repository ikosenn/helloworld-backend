from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from helloworld.common.models import AbstractBase


class UserManager(BaseUserManager):
    """
    A custom user manager for emr
    """
    def create_user(
            self, first_name=None, last_name=None, email=None, password=None,
            **extra_fields):
        """
        Creates and saves a User with the given email.
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name, last_name=last_name,
            email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email=None, first_name=None, last_name=None,
                         password=None):
        """
        Creates and saves a User with the given email.
        """

        user = self.create_user(
            first_name,
            last_name,
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBase, AbstractBaseUser):
    """
    A custom user manager for madeasy user
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_fullname(self):
        return " ".join([self.first_name, self.last_name])
