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

        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The Email must be set")
        if not password:
            raise ValueError("The Password must be set")

        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(max_length=25, verbose_name="User Email", unique=True)
    password = models.CharField(max_length=128, verbose_name="User Password")
    name = models.CharField(max_length=15, verbose_name="Usr Name")
    nick_name = models.CharField(max_length=15, verbose_name="User Nick Name")
    last_login = models.DateTimeField(auto_now_add=True, verbose_name="Last Login Time")
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    # is_active = True

    def __str__(self):
        return self.email

    def get_username(self):
        return self.name

    def get_nickname(self):
        return self.nick_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

