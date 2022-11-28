from random import choice

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404


# def show_departments(request, *args, **kwargs):
#     print(f'{args} - args')
#     print(f'{kwargs} - kwargs')
#     body = f'path = {request.path}, args = {args}, kwargs = {kwargs}'
#     return HttpResponse(body)

def show_departments(request, department_id):
    # print(request.method)
    # print(request.GET)
    # print(request.POST)
    # print(request.get_port())
    # print(request.get_host())
    # print(request.headers)
    body = f'path = {request.path}, id = {department_id}'
    return HttpResponse(body)


def show_departments_by_id(request, department_id):
    context = {
        'page_title': "Departments",
        'method': request.method,
        'ordered_by': request.GET.get('order_by', 'name'),
        'department_id': department_id,
    }
    # http://127.0.0.1:8000/departments/2/?order_by=id
    return render(request, 'departments/all.html', context)
    # if department_id == 1:
    #     department_name = "Developers"
    # elif department_id == 2:
    #     department_name = "Trainers"
    # else:
    #     department_name = None
    # html = f"" \
    #        "<html><body>" \
    #        f"<h1> Department name: {department_name}, Department id: {department_id} </h1>" \
    #        f"</html></body>"
    # return HttpResponse(html)


def redirect_to_first_department(request):
    # possible_order_by = ['name', 'age', 'id']
    # order_by = choice(possible_order_by)
    to = "https://www.softuni.bg"
    # return redirect(to)
    return redirect('show departments', department_id=2)


def show_not_found(request):
    # status_code = 404
    # return HttpResponse("Error", status=status_code)
    # get_object_or_404()
    raise Http404("Not found!")