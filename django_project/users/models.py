from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManagerForEmail(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            e_message = "Поле Email обязательно"
            raise ValueError(e_message)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            e_message = "Суперпользователь должен иметь is_staff=True."
            raise ValueError(e_message)

        if extra_fields.get("is_superuser") is not True:
            e_message = "Суперпользователь должен иметь is_superuser=True."
            raise ValueError(e_message)

        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractUser):
    last_name = None
    first_name = None

    bio = models.TextField(
        verbose_name="биография",
        default="",
        validators=[
            MaxLengthValidator(2048),
        ],
    )
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=32,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer.\
            Letters, digits and @/./+/-/_ only.",
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        verbose_name="почта",
        unique=True,
    )
    is_public_profile = models.BooleanField(
        verbose_name="возможность просмотра профиля другими игроками",
        default=True,
    )

    objects = UserManagerForEmail()

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.username
