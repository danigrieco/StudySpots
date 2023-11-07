from django import template
register = template.Library()

@register.filter
def in_any_groups(all_groups):
    return len(all_groups) > 0
