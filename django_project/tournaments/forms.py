import mdeditor
from django import forms

from tournaments.models import TournamentModel, RequestTeamForTournamentModel
from teams.models import TeamModel


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
    is_closed_for_requests = forms.BooleanField(
        label="Можно ли подать заявку на участие в турнир",
        required=False,
        widget=forms.CheckboxInput(),
    )

    class Meta:
        model = TournamentModel
        fields = [
            "title",
            "rules",
            "description",
            "is_closed_for_requests",
        ]


class RequestTeamTournamentForm(forms.Form):
    team = forms.ModelChoiceField(
        label="Выбирите команду от которой посылаете запрос на участие",
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "placeholder": "Выбери команду",
            },
        ),
        queryset=TeamModel.objects,
        required=False,
    )

    def set_team_selecting(self, leader_user):
        self.fields["team"].queryset = TeamModel.objects.filter(
            leader=leader_user,
        )

    class Meta:
        fields = [
            "team",
        ]
