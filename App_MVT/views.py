from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from App_MVT.models import Persona
from App_MVT.models import Miembro
from App_MVT.models import Familiar

# Create your views here.

def familiar(self):

    #persona1 = Persona(nombre = "Isaac Jimenez", fecha_nac = "5/12/1985", edad = 37)
    #persona1.save()

    #persona2 = Persona(nombre = "Ricardo Jimenez", fecha_nac = "7/2/1987", edad = 35)
    #persona2.save()


    #persona3 = Persona(nombre = "Pedro Jimenez", fecha_nac = "5/4/1988", edad = 34)
    #persona3.save()


    familiar1 = Familiar(nombre = "Pedro Jimenez", fecha_nac = '1988-4-5', edad = 34)
    familiar1.save()

    familiar2 = Familiar(nombre = "Ricardo Jimenez", fecha_nac = '1987-2-7', edad = 35)
    familiar2.save()

    familiar3 = Familiar(nombre = "Isaac Jimenez", fecha_nac = '1984-12-5', edad = 37)
    familiar3.save()

    nombre1 = familiar1.nombre
    fecha1 = familiar1.fecha_nac
    edad1 = familiar1.edad

    nombre2 = familiar2.nombre
    fecha2 = familiar2.fecha_nac
    edad2 = familiar2.edad

    nombre3 = familiar3.nombre
    fecha3 = familiar3.fecha_nac
    edad3 = familiar3.edad

    dicc = {'nombre1':nombre1, 
            'fecha1':fecha1, 
            'edad1':edad1, 
            'nombre2':nombre2, 
            'fecha2':fecha2, 
            'edad2':edad2, 
            'nombre3':nombre3, 
            'fecha3':fecha3, 
            'edad3':edad3, 
    
    
    }

    plantilla = loader.get_template('template_MVT_RJ.html')
    documento = plantilla.render(dicc)  
    return HttpResponse(documento)

    #texto = f"Registro creado: {familiar1.nombre} {familiar1.fecha_nac} {familiar1.edad}"
    #return HttpResponse(texto)

    

