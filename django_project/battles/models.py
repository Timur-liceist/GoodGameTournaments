from django.db import models
from teams.models import TeamModel


class BattleModel(models.Model):
    CHOICES_STATUS = [
        ("win_first", "Победа первой команды"),
        ("win_second", "Победа второй команды"),
        ("draw", "Ничья"),
        ("soon", "Ещё не был проведён"),
        ("problem", "Не состоялса по техническим причинам"),
    ]
    team_first = models.ForeignKey(
        TeamModel,
        verbose_name="первая команда",
        on_delete=models.SET_NULL,
        null=True,
        related_name="battles_team_first",
    )
    team_second = models.ForeignKey(
        TeamModel,
        verbose_name="вторая команда",
        on_delete=models.SET_NULL,
        null=True,
        related_name="battles_team_second",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата и время создания",
    )
    status = models.CharField(
        choices=CHOICES_STATUS,
        verbose_name="статус проведения",
        blank=False,
        max_length=64,
    )
    judges = models.ManyToManyField(
        "users.UserModel",
        verbose_name="судьи",
        related_name="battles_by_judge",
        blank=True,
    )
    start_datetime = models.DateTimeField(
        verbose_name="дата и время начала",
    )
    proof = models.TextField(
        verbose_name="доказательство",
        default="",
    )

    class Meta:
        verbose_name = "сражение"
        verbose_name_plural = "сражения"

    def __str__(self):
        return f"{self.created_at} {self.status}"
