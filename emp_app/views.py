from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Employee, Role, Department
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html',context)

def get_departments(request):
    departments = list(Department.objects.values('id', 'name'))
    return JsonResponse({'departments': departments})

def get_roles(request):
    roles = list(Role.objects.values('id', 'name'))
    return JsonResponse({'roles': roles})

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role= int(request.POST['role'])
        new_emp = Employee(first_name = first_name, last_name = last_name, salary = salary, bonus = bonus, phone = phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save()
        messages.success(request, 'Employee added successfully!')
        all_emps = Employee.objects.all()
        return render(request, 'all_emp.html', {'emps': all_emps})
    elif request.method=='GET':
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'add_emp.html', {
            'departments': departments,
            'roles': roles
        })
    else:
        return HttpResponse('An Exception Occured! Employee Has Not Been Added')


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method=="POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        context = {
            'emps' : emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
    
def edit_emp(request,emp_id=0):
    if emp_id:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = int(request.POST['salary'])
            bonus = int(request.POST['bonus'])
            phone = int(request.POST['phone'])
            dept = int(request.POST['dept'])
            role= int(request.POST['role'])

            edit = Employee.objects.get(id=emp_id)
            edit.first_name = first_name
            edit.last_name = last_name
            edit.salary = salary
            edit.dept_id = dept
            edit.role_id = role
            edit.bonus = bonus
            edit.phone = phone
            edit.save()
            return redirect("/all_emp")
        emp_to_be_edited = Employee.objects.get(id=emp_id)
        departments = Department.objects.all()
        roles = Role.objects.all()
        context1={
            "d": emp_to_be_edited,
            "departments": departments,
            "roles": roles
        }
        return render(request,"edit_emp.html", context1)
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'edit_emp.html', context)