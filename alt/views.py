from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from django.urls import reverse
from alt.models import UserModel


# Create your views here.
def index(request):
    return HttpResponseRedirect('search')


def search(request): 
    if request.method == 'POST':
        result = UserModel.users.filter(
                Q(employee_id__contains=request.POST['search_key']) |
                Q(employee_iex_id__contains=request.POST['search_key'])|
                Q(employee_name__contains=request.POST['search_key']) |
                Q(employee_wave__contains=request.POST['search_key']) |
                Q(employee_team_leader__contains=request.POST['search_key']) |
                Q(employee_manager__contains=request.POST['search_key']) |
                Q(employee_hire_date__contains=request.POST['search_key'])
        )
   
        context = {'employees': result}
        return render(request, 'alt/search.html', context=context)
    elif request.method == 'GET':
        return render(request, 'alt/search.html')


def users(request):
    if request.method == 'POST':
        new_user = UserModel()
        new_user.employee_id = request.POST['employee_id']
        new_user.employee_iex_id = request.POST['employee_iex_id']
        new_user.employee_name = request.POST['employee_name']
        new_user.employee_wave = request.POST['employee_wave']
        new_user.employee_team_leader = request.POST['employee_team_leader']
        new_user.employee_manager = request.POST['employee_manager']
        new_user.employee_hire_date = request.POST['employee_hire_date']
        new_user.save()

    return render(request, 'alt/users.html')


def employee(request, employee_id):
    try:
        result = UserModel.users.get(pk=employee_id)
    except ObjectDoesNotExist:
        raise Http404()
    else:
        return render(request, 'alt/employee.html', context={'employee_obj': result})