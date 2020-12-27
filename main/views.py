from django.http import HttpResponse
from datetime import datetime
def welcome(request):
    documento = '''<html>
    <body>
    <h1>
    Bievenido a mi primera pagina con Django
    </h1>
    </body>
    </html>'''
    return HttpResponse(documento)


def goodbye(request):
    documento = '''<html>
    <body>
    <h1>
    Nos vemos espero verte pronto
    </h1>
    </body>
    </html>'''
    return HttpResponse(documento)


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