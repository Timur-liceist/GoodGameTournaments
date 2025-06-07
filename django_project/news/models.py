from core.models import AbstractNews
from django.db import models
from users.models import UserModel


class GeneralNewsModel(AbstractNews):
    author = models.ForeignKey(
        UserModel,
        verbose_name="автор",
        on_delete=models.SET_NULL,
        null=True,
        related_name="general_news_by_user",
    )

    class Meta:
        verbose_name = "общая новость сайта"
        verbose_name_plural = "общие новости сайта"

    def __str__(self):
        return self.title
