from django import template

register = template.Library()


@register.filter(name= 'addClass')
def add_class(field):
    return field.as_widget(attrs={'class': field.css_classes('form-control')})
