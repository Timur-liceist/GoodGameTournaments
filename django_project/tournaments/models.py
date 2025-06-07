import django.core.validators
from django.db import models
from mdeditor.fields import MDTextField
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
    count_of_members_in_team = models.PositiveSmallIntegerField(
        verbose_name="количество участников в одной команде",
        default=1,
        validators=[
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(32),
        ],
    )
    count_of_teams = models.PositiveSmallIntegerField(
        verbose_name="количество команд",
        default=1,
        validators=[
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(100),
        ],
    )
    created_at = models.DateTimeField(
        verbose_name="дата и время создания",
        auto_now_add=True,
    )
    start_datetime = models.DateTimeField(
        verbose_name="дата и время начала",
    )
    end_datetime = models.DateTimeField(
        verbose_name="дата и время начала",
    )
    is_closed_for_requests = models.BooleanField(
        verbose_name="можно ли ещё зарегистрироваться",
        default=False,
    )

    class Meta:
        verbose_name = "турнир"
        verbose_name_plural = "турниры"

    def __str__(self):
        return f"'{self.title}' by '{self.owner.username}'"
