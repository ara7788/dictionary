from django import template
from lection.models import Lection

register = template.Library()

@register.simple_tag()
def get_lections():
    return list(Lection.objects.order_by('title'))