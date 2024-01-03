from django import template
from framework.models import Framework

register = template.Library()

@register.simple_tag()
def get_frameworks():
    return list(Framework.objects.order_by('frameworkgroup'))