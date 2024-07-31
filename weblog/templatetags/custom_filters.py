import bleach
from django import template

register = template.Library()

ALLOWED_TAGS = ['b', 'i', 'u', 'em', 'strong', 'p', 'br', 'ul', 'li', 'ol','span']
ALLOWED_ATTRIBUTES = {
    '*': ['style'],  
}

@register.filter(name='clean_html')
def clean_html(value):
    return bleach.clean(value, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
