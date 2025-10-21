from django.db import models
from mdeditor.fields import MDTextField


class AbstractNews(models.Model):
    title = models.CharField(
        verbose_name="заголовок",
        max_length=127,
    )
    content = MDTextField(
        verbose_name="содержимое",
    )
    created_at = models.DateTimeField(
        verbose_name="дата и время создания",
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class LikeToNews(models.Model):
    user = models.ForeignKey(
        verbose_name="пользователь",
        to="users.UserModel",
        on_delete=models.CASCADE,
        related_name="likes_to_news",
    )

    class Meta:
        abstract = True


class DislikeToNews(models.Model):
    user = models.ForeignKey(
        verbose_name="пользователь",
        to="users.UserModel",
        on_delete=models.CASCADE,
        related_name="likes_to_news",
    )

    class Meta:
        abstract = True
