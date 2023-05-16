from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request, department_id=None, slug_info=None):
    context = {
        'department_id': department_id,
        'slug_info': slug_info,
        'request': request,
        'order_by': request.GET.get('order_by', 'name'),
    }
    return render(request, 'urls.html', context)


# http://127.0.0.1:8000/urls/10/test-5?order_by=id

# def redirect_to_first_department(request):
#     return redirect('https://softuni.bg/')


# def redirect_to_first_department(request):
#     return redirect('show departments')

def redirect_to_first_department(request):
    return redirect('show department details', department_id=13)


def show_not_found(request):
    # return HttpResponseNotFound("Page not found!")
    # status_code = 404
    # return HttpResponse("Error", status=status_code)
    raise Http404("Not Found!")

