from django import template

register = template.Library()


@register.inclusion_tag('tags/nav.html', name='app_nav')
def create_navigation(*args):
    context = {
        'url_tags': args
    }
    return context
