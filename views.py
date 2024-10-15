from django.shortcuts import render
from django.http import HttpResponse
from EMS.models import Employee22


# class Employee22:

#     def __init__(self):

#         self.eid=0
#         self.name=''
#         self.age=''
#         self.address=''
#         self.mobileno=''

# def get_emp_data(n):

#     new_list=[]
        
#     for i in range(n+1):

#         emp=Employee22()
            
#         emp.eid=1+int(i)
#         emp.name='sachin'+str(i)
#         emp.age=22+ int(i)
#         emp.address='Delhi'+str(i)
#         emp.mobileno='979843652'+str(i)
#         new_list.append(emp)

#     return new_list

# Create your views here.

def view_home(request):
    if request.method=='GET':
        #resp=HttpResponse('<h1>thanks to Home page</h1>')
        resp=render(request,'EMS/home.html')
        return resp
    
    elif request.method=='POST':
        if 'btnadd' in request.POST:
            emp=Employee22()
            emp.name=request.POST.get('txtname','NA')
            emp.age=int(request.POST.get('txtage',0))
            emp.address=request.POST.get('txtadd','NA')
            emp.mobileno=request.POST.get('txtmobile','NA')

            emp.save()
        
            resp=HttpResponse('<h1>Your Form submited Successfully>></h1>')
            return resp
        
        elif 'btnsearch' in request.POST:
            
            eid= int(request.POST.get('txteid',0))
            emp=Employee22.objects.get(id=eid)
            
            d1={'emp':emp}
            
            resp=render(request,'EMS/home.html',context=d1)
            return resp
        

        elif 'btnupdate' in request.POST:

            emp1=Employee22()
            emp1.id=int(request.POST.get('txteid',0))
            if Employee22.objects.filter(id=emp1.id).exists():

                emp1.name=request.POST.get('txtname','NA')
                emp1.age=int(request.POST.get('txtage',0))
                emp1.address=request.POST.get('txtadd','NA')
                emp1.mobileno=request.POST.get('txtmobile','NA')

                emp1.save()
        
                resp=HttpResponse('<h1>Your Form Updated Successfully>></h1>')
                return resp
        
        elif 'btndelete' in request.POST:
            emp2=Employee22()
            emp2.id=int(request.POST.get('txteid',0))
            if Employee22.objects.filter(id=emp2.id).delete():

                resp=HttpResponse('<h1>Your Form Deleted Successfully>></h1>')
                return resp
        

        elif 'btnshow' in request.POST:

            emp4=Employee22.objects.all()
            d1={"epAll":emp4}

            resp=render(request,'EMS/home.html',context=d1)
            return resp

def view_show(request):
    
    resp=render(request,'EMS/show.html')
   # resp=HttpResponse('<h1>thanks to Employee page</h1>')
    return resp

def view_dtl(request):
     #emply=get_emp_data(7)
     d1={'epm':emply}
     resp=render(request,'EMS/dtl.html',context=d1)
     return resp

