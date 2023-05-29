from django.core.exceptions import ValidationError

from temp_project.forms.models import Todo


def validate_max_todos_per_person(assignee):
    if assignee.todo_set.count() >= Todo.MAX_TODOS:
        raise ValidationError(f"{assignee} already has max todos assigned")