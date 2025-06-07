from django.db import models
from users.models import UserModel


class Member(models.Model):
    user = models.ForeignKey(
        UserModel,
        verbose_name="пользователь",
        related_name="members_by_user",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        verbose_name="дата и время создания",
        auto_now_add=True,
    )
    role_name = models.CharField(
        verbose_name="название роли участника",
        max_length=255,
    )

    class Meta:
        verbose_name = "участник"
        verbose_name_plural = "участники"

    def __str__(self):
        return self.user.email


class TeamModel(models.Model):
    name = models.CharField(
        verbose_name="название команды",
        max_length=255,
    )
    leader = models.ForeignKey(
        UserModel,
        verbose_name="лидер",
        on_delete=models.CASCADE,
        related_name="teams_by_leader",
    )
    members = models.ManyToManyField(
        Member,
        related_name="team_by_member",
    )
    created_at = models.DateTimeField(
        verbose_name="дата и время создания",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "команда"
        verbose_name_plural = "команды"

    def __str__(self):
        return self.name
