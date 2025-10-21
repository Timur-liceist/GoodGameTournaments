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
