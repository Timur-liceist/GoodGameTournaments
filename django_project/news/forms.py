from django import forms
from mdeditor.widgets import MDEditorWidget

from news.models import NewsModel


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsModel

        fields = [
            "title",
            "content",
        ]
        widgets = {
            "content": MDEditorWidget(),
        }
