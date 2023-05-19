from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from temp_project.models_demo.models import Employee, Department


def index(request):
    x = list(Employee.objects.all())
    y = list(Employee.objects.filter(id=5))
    z = list(User.objects.all())
    print(y)
    print([x1.first_name for x1 in x])
    context = {
        'employees': Employee.objects.all(),
        'one_employee': list(Employee.objects.filter(id=3))[0],
        'non_it': Employee.objects.exclude(department_id=1).order_by('department_id'),
        'department': Department.objects.get(pk=1),
        'by_year': Employee.objects.filter(birthdate__year__lte=1990).order_by('first_name'),
        'by_department': Employee.objects.filter(department__name='IT').order_by('first_name'),
        'departments_new': Department.objects.all()
        # 'em-pr': Employee.projects()
    }
    return render(request, 'models.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug),
    }
    return render(request, 'department-details.html', context)

# Employee.objects.raw('SQL code here')
# Employee.objects.all() # select
# Employee.objects.create() # insert
# Employee.objects.filter() # update + where
# Employee.objects.update() # update
