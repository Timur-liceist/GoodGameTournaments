import mdeditor
from django import forms

from tournaments.models import TournamentModel


class TournamentCreateForm(forms.ModelForm):
    title = forms.CharField(
        label="Название турнира",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите название турнира",
            },
        ),
        required=True,
    )
    rules = forms.CharField(
        label="Правила турнира",
        widget=mdeditor.fields.MDEditorWidget(
            attrs={
                "class": "form-control",
                "placeholder": "Введите правила турнира",
            },
        ),
        required=False,
    )
    description = forms.CharField(
        label="Описание турнира",
        widget=mdeditor.fields.MDEditorWidget(
            attrs={
                "class": "form-control",
                "placeholder": "Введите описание турнира",
            },
        ),
        required=False,
    )
    start_datetime = forms.DateTimeField(
        label="Дата и время начала проведения турнира",
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "type": "datetime-local",
                "placeholder": "Выберите дату и время начала проведения",
            },
        ),
        required=True,
    )
    end_datetime = forms.DateTimeField(
        label="Дата и время окончания турнира",
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "type": "datetime-local",
                "placeholder": "Выберите дату и время окончания проведения",
            },
        ),
        required=True,
    )
    count_of_teams = forms.IntegerField(
        label="Количество команд",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите количество команд",
            },
        ),
        required=True,
        initial=1,
    )
    count_of_members_in_team = forms.IntegerField(
        label="Количество участников в команде",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите количество участников в команде",
            },
        ),
        required=True,
        initial=1,
    )

    class Meta:
        model = TournamentModel
        fields = [
            "title",
            "rules",
            "description",
            "start_datetime",
            "end_datetime",
            "count_of_teams",
            "count_of_members_in_team",
        ]
