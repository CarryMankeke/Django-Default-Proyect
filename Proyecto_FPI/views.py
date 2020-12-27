from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

    def __init__(self, name, last_name):

        self.name = name
        self.last_name = last_name


def home(request):
    actual_date = datetime.datetime.now()
    return render(request, 'home.html',{'actual_date':actual_date})


def back_home(request):
    actual_date = datetime.datetime.now()
    return render(request, 'home.html',{'actual_date':actual_date})


def welcome(request):
    p1 = Persona('Camilo', 'Soto')
    themes = ['Templates', 'Models', 'Forms', 'Views', 'App Deploy']
    actual_date = datetime.datetime.now()
    return render(request, 'welcome.html', {'nombre_persona':p1.name, 'apellido_persona':p1.last_name, 'date':actual_date, 'themes':themes})


def goodbye(request):

    return render(request, 'goodbye.html', {})


def date(request):
    actual_date = datetime.datetime.now()
    documento = '''<html>
    <body>
    <h2>
    Fecha y hora actual %s
    </h2>
    </body>
    </html>''' % actual_date
    return HttpResponse(documento)


def YrsOldCalculate(request, edad, agno):

    period = agno - 2020
    suma = edad + period
    documento = '''<html>
    <body>
    <h2>
    En el año %s tendras %s años
    </h2>
    </body>
    </html>''' %(agno, suma)

    return HttpResponse(documento)