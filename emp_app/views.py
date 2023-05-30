from django.shortcuts import render , HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models  import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request, 'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])
        phone =int( request.POST['phone'])
        hired_date = int(request.POST['hire_date'])
        new_emp = Employee(firstname=firstname,lastname=lastname,salary=salary,bonus=bonus,role_id=role,dept_id=dept,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')
    elif request.method=='GET':
         return render(request, 'add_emp.html')
    else:
        return HttpResponse("An exception occured")

def remove_emp(request , emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("employee removed successfully")
        except:
            return HttpResponse("please enter a valid emp id")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request, 'remove_emp.html',context)

