from django.shortcuts import render
from django.http import HttpResponse

def vistaUno(request):
    return HttpResponse("<H1> Aplicacion DOS, vista UNO <H1> <H2> Aplicacion DOS, vista UNO <H2> <H3> Aplicacion DOS, vista UNO <H3> <H4> Aplicacion DOS, vista UNO <H4>")

def vistaDos(request):
    return HttpResponse("<H1> Aplicacion DOS, vista DOS <H1> <H2> Aplicacion DOS, vista DOS <H2> <H3> Aplicacion DOS, vista DOS <H3> <H4> Aplicacion DOS, vista DOS <H4>")