from django.shortcuts import render
from django.http import HttpResponse

def vistaUno(request):
    return HttpResponse("<H1> Aplicacion UNO, vista UNO <H1> <H2> Aplicacion UNO, vista UNO <H2> <H3> Aplicacion UNO, vista UNO <H3> <H4> Aplicacion UNO, vista UNO <H4>")

def vistaDos(request):
    return HttpResponse("<H1> Aplicacion UNO, vista DOS <H1> <H2> Aplicacion UNO, vista DOS <H2> <H3> Aplicacion UNO, vista DOS <H3> <H4> Aplicacion UNO, vista DOS <H4>")