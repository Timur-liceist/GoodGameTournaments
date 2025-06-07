from django.db import models
from mdeditor.fields import MDTextField
from users.models import UserModel


class NewsModel(models.Model):
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
    author = models.ForeignKey(
        UserModel,
        verbose_name="автор",
        on_delete=models.SET_NULL,
        null=True,
        related_name="news_by_author",
    )

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"

    def __str__(self):
        return self.title
