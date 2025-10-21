from django import forms
from django.core.validators import MaxLengthValidator

from teams.models import TeamModel


class TeamForm(forms.ModelForm):
    name = forms.CharField(
        label="Название команды",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "Placeholder": "Введите название команды",
            },
        ),
    )

    class Meta:
        model = TeamModel
        fields = ["name"]


class InviteToTeamByEmailForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "Placeholder": "Введите email",
            },
        ),
    )

    class Meta:
        fields = ["email"]


class ChangeRoleMemberTeamForm(forms.Form):
    role = forms.CharField(
        label="Название роли в команде",
        widget=forms.TextInput(
            attrs={
                "maxlength": "32",
                "class": "form-control",
                "Placeholder": "Введите название роли",
            },
        ),
        validators=[
            MaxLengthValidator(32),
        ],
    )

    class Meta:
        fields = ["role"]
