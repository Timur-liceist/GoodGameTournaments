import django.core.validators
from core.models import AbstractNews
from django.db import models
from mdeditor.fields import MDTextField
from teams.models import TeamModel
from users.models import UserModel


class EventForTimeTable(models.Model):
    name = models.CharField(
        verbose_name="название",
        max_length=255,
    )
    description = MDTextField(
        verbose_name="описание",
        default="",
    )
    start_datetime = models.DateTimeField(
        verbose_name="дата и время начала",
    )
    end_datetime = models.DateTimeField(
        verbose_name="дата и время окончания",
    )
    tournament = models.ForeignKey(
        "TournamentModel",
        verbose_name="турнир",
        on_delete=models.CASCADE,
        related_name="tournament_by_timetable_events",
    )

    class Meta:
        verbose_name = "событие для расписания турнира"
        verbose_name_plural = "события для расписания турнира"

    def __str__(self):
        return f"'{self.name}'"


class TournamentModel(models.Model):
    title = models.CharField(
        verbose_name="название турнира",
        max_length=255,
    )
    owner = models.ForeignKey(
        UserModel,
        verbose_name="владелец",
        related_name="tournaments_by_owner",
        on_delete=models.SET_NULL,
        null=True,
    )
    judges = models.ManyToManyField(
        UserModel,
        verbose_name="судьи",
        related_name="tournaments_by_judges",
        blank=True,
    )
    description = MDTextField(
        verbose_name="описание",
        default="",
    )
    rules = MDTextField(
        verbose_name="правила",
        default="",
    )
    created_at = models.DateTimeField(
        verbose_name="дата и время создания",
        auto_now_add=True,
    )
    is_closed_for_requests = models.BooleanField(
        verbose_name="можно ли ещё подать заявку на участие",
        default=False,
    )
    team_members = models.ManyToManyField(
        "teams.TeamModel",
        related_name="tournaments",
    )

    class Meta:
        verbose_name = "турнир"
        verbose_name_plural = "турниры"

    def __str__(self):
        return f"'{self.title}' by '{self.owner.username}'"


class TournamentNews(AbstractNews):
    tournament = models.ForeignKey(
        TournamentModel,
        verbose_name="турнир",
        on_delete=models.CASCADE,
        related_name="news_by_tournament",
    )
    author = models.ForeignKey(
        UserModel,
        verbose_name="автор",
        on_delete=models.SET_NULL,
        null=True,
        related_name="tournament_news_by_user",
    )

    class Meta:
        verbose_name = "новость турнира"
        verbose_name_plural = "новости турниров"

    def __str__(self):
        return f"{self.title} ({self.tournament.name})"


class RequestTeamForTournamentModel(models.Model):
    CHOICES_STATUS = [
        ("pending", "Ожидается"),
        ("accepted", "Принята"),
        ("rejected", "Отклонена"),
        ("expired", "Просрочена"),
    ]
    team = models.ForeignKey(
        TeamModel,
        on_delete=models.CASCADE,
        verbose_name="команда",
    )
    tournament = models.ForeignKey(
        TournamentModel,
        on_delete=models.CASCADE,
        verbose_name="турнир",
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

    def __str__(self):
        return f"Request {self.team.name} ({self.tournament.name})"
