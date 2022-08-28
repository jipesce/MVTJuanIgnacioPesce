from django.http import HttpResponse
from django.template import Template, Context, loader
from Familiares.models import *

def saludo(request):
  return HttpResponse('Hola Django - Coder')

def familiares(self):

  diccionario = {
    'Familiares': [
      {
      'Nombre': 'Silvina',
      'Apellido': 'Aguirre',
      'Parentesco': 'madre',
      'Edad': 52,
      'Nacimiento': {'anio': '1970', 'mes': '09', 'dia': '28' }
      },
      {
      'Nombre': 'Andres',
      'Apellido': 'Galeano',
      'Parentesco': 'padre',
      'Edad': 55,
      'Nacimiento': {'anio': '1967', 'mes': '06', 'dia': '27' }
      },
      {
      'Nombre': 'Ludmila',
      'Apellido': 'Galeano Aguirre',
      'Parentesco': 'hermana',
      'Edad': 25,
      'Nacimiento': {'anio': '1997', 'mes': '03', 'dia': '24' }
      }
    ]
  }

  plantilla = loader.get_template('template1.html')
  documento = plantilla.render(diccionario)

  # for item in diccionario['Familiares']:
  #   Nacimiento = f"{item['Nacimiento']['anio']}-{item['Nacimiento']['mes']}-{item['Nacimiento']['dia']}"
  #   familiar = Familiares(nombre=item['Nombre'], apellido=item['Apellido'], parentesco=item['Parentesco'], edad=item['Edad'], nacimiento=Nacimiento)
  #   familiar.save()

  return HttpResponse(documento)
