from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
def welcome(request):
    external_doc = open('C:/Users/camil/Documents/GitHub/Django-Default-Proyect/Proyecto_FPI/templates/welcome.html')
    plt = Template(external_doc.read())
    external_doc.close()
    context = Context()
    doc  = plt.render(context)
    return HttpResponse(doc)


def goodbye(request):

    external_doc = open('C:/Users/camil/Documents/GitHub/Django-Default-Proyect/Proyecto_FPI/templates/goodbye.html')
    plt = Template(external_doc.read())
    external_doc.close()
    context = Context()
    doc  = plt.render(context)
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