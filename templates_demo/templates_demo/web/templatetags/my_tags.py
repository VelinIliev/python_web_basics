from django import template
register = template.Library()

from templates_demo.web.views import Student


@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hello, my name is {student.name} and I am {student.age}-years old'


@register.simple_tag(name='simple_tag')
def sample_tag(*args, **kwargs):
    return ", ".join(str(x) for x in (list(args) + list(kwargs.items())))


@register.inclusion_tag('tags/nav.html', name='app_nav', takes_context=True)
def generate_nav(context, *args):
    return {
        'url_names': args,
        # 'context': context
    }
    # return context
