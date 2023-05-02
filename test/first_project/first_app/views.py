from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Employee

# Create your views here.

def index(request):
    #return HttpResponse('Welcome to the underground')
    #dict = {
     #       'insert_me' : 'hi this is from views.py',
      #      'fname' : 'derek',
       #     'lname' : 'grandious',
        #    'age' : '40'

    #}

    emp_list = Employee.objects.order_by('emp_name')
    emp_dict = { 'emp ' : emp_list}

    return render(request, 'first_app/index.html', context=emp_dict)


def about(request):
    return HttpResponse('<h1> weenor </h1>')
