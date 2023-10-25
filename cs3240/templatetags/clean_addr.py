from django import template

register = template.Library()

@register.filter
def clean_addr(address):
    return address.replace(' ','+')