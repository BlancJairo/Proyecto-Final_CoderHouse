from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {}
    http_response = render(
        request = request,
        template_name = 'app_proyecto/index.html',
        context = contexto,
    )
    return http_response


def sobre_mi(request):
    contexto = {}
    http_response = render(
        request = request,
        template_name = 'app_proyecto/sobre_mi.html',
        context = contexto,
    )
    return http_response

