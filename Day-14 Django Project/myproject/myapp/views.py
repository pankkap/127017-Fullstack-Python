from json import load
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# for redirection to requested View

from django.template import loader
from .models import Students

# Create your views here.
# def home(request):
#     return HttpResponse("This is Home Page")


def about(request):
    # return HttpResponse("This is about Page")
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def contact(request):
    return HttpResponse("This is contact Page")


# return template to user instead of Simple Message
# import loader from django.template

# def home(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())


# def home(request):
#     mystudents = Students.objects.all().values()
#     output = ""
#     for i in mystudents:
#         output += i["first_name"]
#     return HttpResponse(output)

def home(request):
    template = loader.get_template('index.html')
    mystudents = Students.objects.all().values()
    # sending content as an Object
    content = {
        'mystudents': mystudents
    }
    return HttpResponse(template.render(content, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


# Recieve the Data from client and Store inside the Database

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    student = Students(first_name=x, last_name=y)
    student.save()
    return HttpResponseRedirect(reverse('home'))


def delete(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('home'))


def update(request, id):
    student = Students.objects.get(id=id)
    template = loader.get_template('update.html')
    content = {
        'student': student
    }
    return HttpResponse(template.render(content, request))


def updaterecord(request, id):
    x = request.POST['first']
    y = request.POST['last']
    student = Students.objects.get(id=id)
    student.first_name = x
    student.last_name = y
    student.save()
    return HttpResponseRedirect(reverse('home'))
