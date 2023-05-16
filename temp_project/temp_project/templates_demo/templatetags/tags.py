from django import template

register = template.Library()


@register.simple_tag(name="show_info")
def show_info(student):
    return f'Hello, My name is {student.name} and I am {student.age} years old'


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*url_names):
    context = {
        'url_names': url_names,
    }
    return context
