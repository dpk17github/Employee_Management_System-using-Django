from django.shortcuts import render
from django.shortcuts import HttpResponse,render,redirect
from mng_app.models import Department,Role,Employee 
from django.contrib import messages
# Create your views here.

# home page 
def home(request):
    emp = Employee.objects.all()
    context = {'emp':emp}
    return render(request,"home.html",context)

# view employee function 
def viewEmp(request):
    emp = Employee.objects.all()
    context = {'emp':emp}
    return render(request,"viewEmp.html",context)

# add employee function 
def addEmp(request):
    alldept = Department.objects.all()
    allrole = Role.objects.all()
    context = {'alldept':alldept,'allrole':allrole}
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        department = request.POST.get('department')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        hire = request.POST.get('hire')
        check = request.POST.get('check','off')
        if check == 'on':
            details = Employee(first_name=firstname,last_name=lastname,email=email,salary=salary,bonus=bonus,dept_id=department,
            role_id=role,phone=phone,hire_date=hire)
            details.save()
            messages.success(request,'Employee has been added successfully')
        else:
            messages.warning(request,'Sorry! Please make sure before submit all details')
        # print(firstname,lastname,email,salary,bonus,department,role,phone,hire)
    return render(request,"addEmp.html",context)

# update Employeefunction
def updateEmp(request):
    if request.method == 'POST':
        idswitch = request.POST.get('idswitch','off')
        nameswitch = request.POST.get('nameswitch','off')
        empbyid = Employee.objects.none()
        # empbyname = Employee.objects.none()
        context ={}
        if idswitch == 'on':
            empid = request.POST.get('updatebyid')
            if empid =='':
                empid='0'
            empbyid = Employee.objects.filter(emp_id=empid)
            context.update({'emp':empbyid})
        if nameswitch == 'on':
            empname = request.POST.get('updatebyname')
            if empname =='':
                empname='rrrrrrrrrrrrrrrrrrrrrrr'
            empbyfname = Employee.objects.filter(first_name__icontains=empname)
            empbylname = Employee.objects.filter(last_name__icontains=empname)
            empbyname = empbyfname.union(empbylname)
            empbynameid = empbyname.union(empbyid)
            context.update({'emp':empbynameid})
        if idswitch == 'off' and nameswitch == 'off':
            messages.warning(request,'Please ON atlist one option!') 
            return render(request,'updateEmp.html') 
        return render(request,'updateEmp2.html',context)
    return render(request,'updateEmp.html')

# update Employee3 form function
def updateEmp2(request):
    if request.method =='POST':
        empid = request.POST.get('updateid')
        emp = Employee.objects.filter(emp_id=empid)
        alldept = Department.objects.all()
        allrole = Role.objects.all()
        context = {'emp':emp,'alldept':alldept,'allrole':allrole}
    return render(request,'updateEmp3.html',context)

# final update form submit
def updateEmp3(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        department = request.POST.get('department')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        hire = request.POST.get('hire')
        check = request.POST.get('check','off')
        updateuserid =request.POST.get('updateuserid')
        context = {}
        if check == 'on':
            updateuser = Employee(emp_id=updateuserid,first_name=firstname,last_name=lastname,email=email,salary=salary,bonus=bonus, dept_id=department,
            role_id=role,phone=phone,hire_date=hire)
            updateuser.save()
            messages.success(request,'Update Successfully')
            x = 1
            context.update({'x':x})
        else:
            messages.warning(request,'Sorry! Please make sure before update all details')
            y = 2
            context.update({'y':y})
        return render(request,'updateEmp3.html',context)
    

# remove employee function 
def removeEmp(request):
    allemp = Employee.objects.all()
    context = {'allemp':allemp}
    if request.method == 'POST':
        remove = request.POST['removeEmp']
        remove_emp = Employee.objects.get(emp_id=remove)
        remove_emp.delete()
        messages.success(request,'Employee has been removed successfully')
    return render(request,"removeEmp.html",context)

# filter employee function 
def filterEmp(request):
    alldept = Department.objects.all()
    allrole = Role.objects.all()
    context = {'alldept':alldept,'allrole':allrole}
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('department')
        role = request.POST.get('role')
        email = request.POST.get('email')
        nameswitch = request.POST.get('nameswitch','off')
        departmentswitch = request.POST.get('departmentswitch','off')
        roleswitch = request.POST.get('roleswitch','off')
        emailswitch = request.POST.get('emailswitch','off')
        context2 ={}
        empname = Employee.objects.none()
        emp_name_email = Employee.objects.none()
        emp_name_dept = Employee.objects.none()
        emp_name_role = Employee.objects.none()
        if nameswitch == 'on':
            if name == '':
                name = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            empfname = Employee.objects.filter(first_name__icontains=name)
            emplname = Employee.objects.filter(last_name__icontains=name)
            empname = empfname.union(emplname)
            context2.update({'emp':empname})
        if emailswitch == 'on':
            empemail =Employee.objects.filter(email=email)
            emp_name_email = empemail.union(empname)
            context2.update({'emp':emp_name_email})
        if departmentswitch =='on':
            empdept = Employee.objects.filter(dept=dept)
            emp_name_dept = empdept.union(empname)
            emp_name_dept = emp_name_dept.union(emp_name_email)
            context2.update({'emp':emp_name_dept})
        if roleswitch == 'on':
            emprole = Employee.objects.filter(role=role)
            emp_name_role = emp_name_dept.union(emprole)            
            emp_name_role = emp_name_role.union(empname)            
            emp_name_role = emp_name_role.union(emp_name_email)            
            context2.update({'emp':emp_name_role})
        return render(request,"filterEmp2.html",context2)
    return render(request,"filterEmp.html",context)

# search function 
def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        if search =='':
            search='rrrrrrrrrrr'
        empfname = Employee.objects.filter(first_name__icontains =search)
        emplname = Employee.objects.filter(last_name__icontains =search)
        empname = empfname.union(emplname)
        context2 = {'emp':empname}
    return render(request,'filterEmp2.html',context2)

