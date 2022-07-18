from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from App_MVT.models import Persona
from App_MVT.models import Miembro
from App_MVT.models import Familiar

# Create your views here.

def familiar(self):

    persona1 = Persona(nombre = "Isaac Jimenez", fecha_nac = "5/12/1985", edad = 37)
    persona1.save()

    persona2 = Persona(nombre = "Ricardo Jimenez", fecha_nac = "7/2/1987", edad = 35)
    persona2.save()


    persona3 = Persona(nombre = "Pedro Jimenez", fecha_nac = "5/4/1988", edad = 34)
    persona3.save()


    #familiar1 = Familiar(nombre = "Pedro Jimenez", fecha_nac = 1988/4/5, edad = 34)
    #familiar1.save()

    nombre1 = persona1.nombre
    fecha1 = persona1.fecha_nac
    edad1 = persona1.edad

    nombre2 = persona2.nombre
    fecha2 = persona2.fecha_nac
    edad2 = persona2.edad

    nombre3 = persona3.nombre
    fecha3 = persona3.fecha_nac
    edad3 = persona3.edad

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

    #texto = f"Registro creado: {persona1.nombre} {persona1.fecha_nac} {persona1.edad}"
    #return HttpResponse(texto)

    

