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


class InvitationToTeamModel(models.Model):
    CHOICES_STATUS = [
        ("pending", "Ожидается"),
        ("accepted", "Принята"),
        ("rejected", "Отклонена"),
        ("expired", "Просрочена"),
    ]
    invited_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
    )
    team = models.ForeignKey(
        TeamModel,
        on_delete=models.CASCADE,
        verbose_name="команда",
    )
    created_at = models.DateTimeField(
        verbose_name="дата и время отправки",
        auto_now_add=True,
    )
    status = models.CharField(
        verbose_name="статус",
        max_length=32,
        choices=CHOICES_STATUS,
        default="pending",
    )

    class Meta:
        verbose_name = "заявка команды на участие в турнире"
        verbose_name_plural = "заявки команды на участие в турнире"
