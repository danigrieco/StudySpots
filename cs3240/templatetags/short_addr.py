from django import template

register = template.Library()

@register.filter
def short_addr(address):
    return address.split(',')[0]