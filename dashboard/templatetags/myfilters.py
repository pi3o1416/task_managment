
from django import template

register = template.Library()

@register.filter
def addclass(value, arg):
    if 'class' not in value.field.widget.attrs:
        return value.as_widget(attrs={'class': arg})
    return value

