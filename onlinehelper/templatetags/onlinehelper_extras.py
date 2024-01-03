from django import template
from onlinehelper.models import OnlineHelper

register = template.Library()

@register.simple_tag()
def get_onlinehelpers():
    return list(OnlineHelper.objects.order_by('title'))