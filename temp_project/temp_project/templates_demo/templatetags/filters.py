from django import template

register = template.Library()


@register.filter('odd')
def get_odd(values):
    return [x for x in values if x % 2 == 1]


@register.filter('app_style')
def format_to_app_style(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')
