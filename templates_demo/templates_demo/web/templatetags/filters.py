from datetime import datetime

from django.template import Library

register = Library()


@register.filter('odd')
def get_odd(values):
    return [x for x in values if x % 2 == 1]

@register.filter('app_style')
def format_to_app_style(date):
    return date.strftime("%d-%m-%Y %H:%M")