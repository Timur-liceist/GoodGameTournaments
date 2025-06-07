import markdown
from django import template

register = template.Library()


@register.filter(name="markdown")
def markdown_filter(value):
    extensions = [
        "tables",
    ]
    return markdown.markdown(
        value,
        extensions=extensions,
    )
