import re
from django import template
from django.core.urlresolvers import reverse, resolve


register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name):
    request = context['request']
    if resolve(request.path).url_name == url_name:
        return 'active'
    return ''