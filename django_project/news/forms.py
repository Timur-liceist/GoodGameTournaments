from django import forms
from mdeditor.widgets import MDEditorWidget

from news.models import GeneralNewsModel


class NewsForm(forms.ModelForm):

    class Meta:
        model = GeneralNewsModel

        fields = [
            "title",
            "content",
        ]
        widgets = {
            "content": MDEditorWidget(),
        }
