from django import template
from django.contrib.humanize.templatetags import humanize

register = template.Library()

@register.filter(name='age')
def age(created_at):
    return humanize.naturaltime(created_at)