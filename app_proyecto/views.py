from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from app_proyecto.models import autos, Camionetas, Camiones 
from app_proyecto.forms import form




class autosListView(ListView):
    model = autos
    template_name='app_proyecto/lista_autos.html'

class autoCreateView(CreateView):
    model = autos
    fields = ('marca', 'modelo', 'ano', 'color', 'equipamiento', 'descripcion')
    success_url = reverse_lazy('autos')

class autoDeleteView(DeleteView):
    model = autos
    success_url = reverse_lazy('autos')

class autoDatailView(DetailView):
    model = autos

class autoUpdateView(UpdateView):
    model = autos
    fields = ('marca', 'modelo', 'ano', 'color', 'equipamiento', 'descripcion')
    success_url = reverse_lazy('autos')

def buscar_auto (request):
    
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        auto = autos.objects.filter(modelo__icontains=busqueda)
        contexto = { 
        "object_list" : auto,
        }
    http_response = render(
        request = request,
        template_name = 'app_proyecto/lista_autos.html',
        context = contexto,
    )
    return http_response

#Clases para camiones
class camionetasListView(ListView):
    model = Camionetas
    template_name='app_proyecto/lista_camionetas.html'

class camionetasCreateView(CreateView):
    model = Camionetas
    fields = ('marca', 'modelo', 'ano', 'color', 'equipamiento', 'descripcion')
    success_url = reverse_lazy('camionetas')

class camionetasDeleteView(DeleteView):
    model = Camionetas
    success_url = reverse_lazy('camionetas')

class camionetasDatailView(DetailView):
    model = Camionetas

class camionetasUpdateView(UpdateView):
    model = Camionetas
    fields = ('marca', 'modelo', 'ano', 'color', 'equipamiento', 'descripcion')
    success_url = reverse_lazy('camionetas')

def buscar_camionetas (request):
    
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        camionetas = Camionetas.objects.filter(modelo__icontains=busqueda)
        contexto = { 
        "object_list" : camionetas,
        }
    http_response = render(
        request = request,
        template_name = 'app_proyecto/lista_camionetas.html',
        context = contexto,
    )
    return http_response

#Clases para camiones
class camionesListView(ListView):
    model = Camiones
    template_name='app_proyecto/lista_camiones.html'

class camionesCreateView(CreateView):
    model = Camiones
    fields = ('marca', 'modelo', 'ano', 'color', 'equipamiento', 'descripcion')
    success_url = reverse_lazy('camiones')

class camionesDeleteView(DeleteView):
    model = Camiones
    success_url = reverse_lazy('camiones')

class camionesDatailView(DetailView):
    model = Camiones

class camionesUpdateView(UpdateView):
    model = Camiones
    fields = ('marca', 'modelo', 'ano', 'color', 'equipamiento', 'descripcion')
    success_url = reverse_lazy('camiones')

def buscar_camiones (request):
    
    if request.method == "POST":
        data=request.POST
        busqueda = data["busqueda"]
        camiones = Camiones.objects.filter(modelo__icontains=busqueda)
        contexto = { 
        "object_list" : camiones,
        }
    http_response = render(
        request = request,
        template_name = 'app_proyecto/lista_camiones.html',
        context = contexto,
    )
    return http_response
