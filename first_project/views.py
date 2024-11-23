from django.http import HttpResponse
from django.shortcuts import render

def firstView(request):
    # data = {
    #     'name':"md omar sharif ",
    #     'title':"first",
    #     'student':[
    #         'omar','sami','eman ali'
    #     ],
    #     'student_details':[
    #         {'name':"md omar sharif",'roll':664618,'CGPA':1.00,'contact':1795106871},
    #         {'name':"md eman ali",'roll':664617,'CGPA':2.00,'contact':1795106871},
    #         {'name':"sami",'roll':664615,'CGPA':3.00,'contact':1795106871}
        # ]
    # }
    return render(request,'index.html',)

def registerview(request):
    return render(request, 'registration.html')

def contact (request):
    return render(request,'contact.html')

def admission(request):
    return render(request,'admission.html')

def loginpage(request):
    return render(request,'login.html')
