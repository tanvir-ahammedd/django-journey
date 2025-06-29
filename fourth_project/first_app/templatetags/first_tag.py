from django import template

register = template.Library()

@register.filter(name='change_name')
def my_template(value, arg):
    if arg == 'change':
        value = 'Rahim'
        return value
    if arg == 'title':
        return value.title()