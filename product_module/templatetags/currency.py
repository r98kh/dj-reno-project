from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter(name='currency')
def currency(price):
    price = intcomma(price, use_l10n=False)
    return f'{price} تومان'
