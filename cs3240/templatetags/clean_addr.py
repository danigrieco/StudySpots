from django import template
import urllib.parse
register = template.Library()

@register.filter(is_safe=True)
def clean_addr(to_print):
    return urllib.parse.quote(to_print).replace(' ', '+')
