from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator

from users.models import UserModel


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            },
        ),
        required=True,
    )
    email = forms.EmailField(
        label="Почта",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email",
            },
        ),
        validators=[
            MaxLengthValidator(254),
        ],
        required=True,
    )
    bio = forms.CharField(
        label="О себе(Необязательно)",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Расскажите о себе",
                "rows": 3,
            },
        ),
        required=False,
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите пароль",
            },
        ),
        required=True,
    )
    password_repeat = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Повторите пароль",
            },
        ),
        required=True,
    )

    class Meta:
        model = UserModel
        fields = [
            "username",
            "email",
            "bio",
            "password",
            "password_repeat",
        ]

    def clean_password(self):
        password = self.cleaned_data.get("password")
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages) from e
        return password

    def clean_username(self):
        username = self.cleaned_data.get("username")
        repeated_user = UserModel.objects.filter(username=username).first()
        if repeated_user:
            message_for_exception = "С таким именем пользователь уже существует"  # noqa: E501
            raise forms.ValidationError(
                message_for_exception,
            )
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")

        if password and password_repeat and password != password_repeat:
            message_for_exception = "Пароли не совпадают."
            raise forms.ValidationError(message_for_exception)


class LoginForm(forms.Form):
    email_or_username = forms.CharField(
        label="Почта или имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control ",
                "placeholder": "Введите email или имя пользователя",
            },
        ),
        required=True,
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control ",
                "placeholder": "Введите пароль",
            },
        ),
        required=True,
    )

    class Meta:
        fields = ["email_or_username", "password"]


class ProfileForm(forms.ModelForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            },
        ),
        required=True,
    )
    email = forms.EmailField(
        label="Почта",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email",
            },
        ),
        validators=[
            MaxLengthValidator(254),
        ],
        required=True,
    )
    bio = forms.CharField(
        label="О себе(Необязательно)",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Расскажите о себе",
                "rows": 3,
            },
        ),
        required=False,
    )
    is_public_profile = forms.BooleanField(
        label="Возможность просмотра профиля другими игроками",
        required=False,
        widget=forms.CheckboxInput(),
    )

    class Meta:
        model = UserModel
        fields = [
            "username",
            "email",
            "bio",
            "is_public_profile",
        ]
