"""
URL configuration for pre_entrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from app_proyecto.views import buscar_auto, autoDeleteView, autoUpdateView, autosListView, autoCreateView, autoDatailView,\
                buscar_camionetas, camionetasUpdateView, camionetasDatailView, camionetasDeleteView, camionetasCreateView, camionetasListView,\
                buscar_camiones, camionesUpdateView, camionesDatailView, camionesDeleteView, camionesCreateView, camionesListView
                
urlpatterns = [
    # Path de autos
    path('lista_autos/', autosListView.as_view(), name="autos"),
    path('subir-autos/', autoCreateView.as_view(), name="subir_autos"),
    path('buscar-autos/', buscar_auto, name="buscar_auto"),
    path('ver-autos/<int:pk>/', autoDatailView.as_view(), name="ver_auto"),
    path('eliminar-autos/<int:pk>/', autoDeleteView.as_view(), name="eliminar_auto"),
    path('editar-autos/<int:pk>/', autoUpdateView.as_view(), name="editar_auto"),

    # Path de camionetas
    path('lista_camionetas/', camionetasListView.as_view(), name="camionetas"),
    path('subir-camionetas/', camionetasCreateView.as_view(), name="subir_camionetas"),
    path('buscar-camionetas/', buscar_camionetas, name="buscar_camionetas"),
    path('ver-camionetas/<int:pk>/', camionetasDatailView.as_view(), name="ver_camionetas"),
    path('eliminar-camionetas/<int:pk>/', camionetasDeleteView.as_view(), name="eliminar_camionetas"),
    path('editar-camionetas/<int:pk>/', camionetasUpdateView.as_view(), name="editar_camionetas"),    
    # Path de camiones
    path('lista_camiones/', camionesListView.as_view(), name="camiones"),    
    path('subir-camiones/', camionesCreateView.as_view(), name="subir_camiones"),
    path('buscar-camiones/', buscar_camiones, name="buscar_camiones"),
    path('ver-camiones/<int:pk>/', camionesDatailView.as_view(), name="ver_camiones"),
    path('eliminar-camiones/<int:pk>/', camionesDeleteView.as_view(), name="eliminar_camiones"),
    path('editar-camiones/<int:pk>/', camionesUpdateView.as_view(), name="editar_camiones"),    
]
