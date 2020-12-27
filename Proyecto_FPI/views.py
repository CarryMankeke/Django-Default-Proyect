from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template


class Persona(object):

    def __init__(self, name, last_name):

        self.name = name
        self.last_name = last_name


def welcome(request):
    p1 = Persona('Camilo', 'Soto')
    themes = ['Templates', 'Models', 'Forms', 'Views', 'App Deploy']
    actual_date = datetime.datetime.now()
    external_doc = get_template('welcome.html')
    doc = external_doc.render({'nombre_persona':p1.name, 'apellido_persona':p1.last_name, 'date':actual_date, 'themes':themes})
    return HttpResponse(doc)


def goodbye(request):
    external_doc = get_template('goodbye.html')
    doc  = external_doc.render({})
    return HttpResponse(doc)


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