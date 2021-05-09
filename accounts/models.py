import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        if not password:
            raise ValueError("The Password must be set")

        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("SuperUser must have is_staff = True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("SuperUser must have is_superuser = True.")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=str(uuid.uuid4()))
    email = models.EmailField(max_length=25, verbose_name="User Email",unique=True)
    password = models.CharField(max_length=64, verbose_name="User Password")
    name = models.CharField(max_length=15, verbose_name="Usr Name")
    nick_name = models.CharField(max_length=15, verbose_name="User Nick Name")
    last_login = models.DateTimeField(auto_now_add=True, verbose_name="Last Login Time")
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    is_active = True

    def __str__(self):
        return self.email

    def get_username(self):
        return self.name

    def get_nickname(self):
        return self.nick_name
