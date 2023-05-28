from django.test import TestCase
from app_proyecto.models import autos

class autosTests(TestCase):
    #auto correcto
    def test_creacion_auto_1(self):
        auto=autos(marca='ford', modelo='fiesta', ano= '2015', color='rojo', equipamiento= 'full', descripcion= 'nada para hacerle', creador= "autos.creador")
        auto.save()

        #comprobamos la creacion de un auto
        self.assertEqual(autos.objects.count(), 1)
        self.assertEqual(autos.marca, 'ford')
        self.assertEqual(autos.modelo, 'fiesta')
        self.assertEqual(autos.ano, 2015)
        self.assertEqual(autos.color, 'rojo')
        self.assertEqual(autos.equipamiento, 'full')
        self.assertEqual(autos.descripcion, 'nada para hacerle')
        self.assertEqual(autos.creador, "autos.creador")

    def test_creacion_auto_2(self):
        auto=autos(marca='ford', modelo='fiesta', ano= '20152', color='rojo', equipamiento= 'full', descripcion= 'nada para hacerle', creador= "autos.creador")
        auto.save()

        #comprobamos la creacion de un auto
        self.assertEqual(autos.objects.count(), 0) 


