from django import template

register = template.Library()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']


@register.filter(name='dateFormat')
def date_format(date):
    year, month, day = str(date).split('-')
    return months[int(month)], year , day
