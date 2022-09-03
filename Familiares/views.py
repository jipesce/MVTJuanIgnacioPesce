from django.shortcuts import render

# Create your views here.
def familiares(self):

  BUENOS_AIRES_TZ = datetime.now(timezone('America/Argentina/Buenos_Aires'))

  diccionario = {
    'FechaActual': BUENOS_AIRES_TZ,
    'Familiares': [
      {
      'Nombre': 'Silvina',
      'Apellido': 'Aguirre',
      'Parentesco': 'madre',
      'Edad': 51,
      'Nacimiento': {'anio': 1970, 'mes': '09', 'dia': '28' }
      },
      {
      'Nombre': 'Andres',
      'Apellido': 'Galeano',
      'Parentesco': 'padre',
      'Edad': 55,
      'Nacimiento': {'anio': 1967, 'mes': '06', 'dia': '27' }
      },
      {
      'Nombre': 'Ludmila',
      'Apellido': 'Galeano Aguirre',
      'Parentesco': 'hermana',
      'Edad': 25,
      'Nacimiento': {'anio': 1997, 'mes': '03', 'dia': '24' }
      }
    ]
  }

  plantilla = loader.get_template('template1.html')
  documento = plantilla.render(diccionario)

  for item in diccionario['Familiares']:
    Nacimiento = f"{item['Nacimiento']['anio']}-{item['Nacimiento']['mes']}-{item['Nacimiento']['dia']}"
    familiar = Familiares(nombre=item['Nombre'], apellido=item['Apellido'], parentesco=item['Parentesco'], edad=item['Edad'], nacimiento=Nacimiento)
    familiar.save()

  return HttpResponse(documento)

def mostrarFamiliares(request):
  #Trae todos los familiares de la base de datos
  listaDeFamilia = Familiar.objects.all() #codigo importante

  diccionario = {
    'FechaActual': BUENOS_AIRES_TZ,
    'Familiares': listaDeFamilia
  }

  plantilla = loader.get_template("muestraFamilia.html")
  documento = plantilla.render(diccionario)

  return HttpResponse(documento)