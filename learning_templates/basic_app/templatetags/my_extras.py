from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    Cuts values of arg from strings
    """
    return value.replace(arg,'')

#register.filter('cut',cut)