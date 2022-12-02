from django.shortcuts import render, get_object_or_404, redirect

from models_demos.web.models import Employee, Department


def index(request):
    # 'employees2': Employee.objects.filter(age__gte=24).order_by('level'),
    # 'employees2': Employee.objects.filter(department__name="IT"),
    context = {
        'employees': Employee.objects.all(),
        'employees2': Employee.objects.all(),
        'department': Department.objects.get(pk=1)
    }
    return render(request, 'index.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')


def department_details(request, slug):
    context = {
        'department': get_object_or_404(Department, slug=slug)
    }
    return render(request, 'department-details.html', context)