from django import template

register = template.Library()

@register.filter
def format_name(name):
    return name.capitalize()
