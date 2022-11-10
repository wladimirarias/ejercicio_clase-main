from django.http import HttpResponse
from appcoder.models import Curso
from appcoder.models import Profesor
from django.shortcuts import render
from appcoder.forms import ProfesorFormulario


def inicio(request):
    return render (request, "appcoder/index.html")
    
def cursos(request):
    return render(request, "appcoder/cursos.html")

def creacion_curso(request):
    if request.method == 'POST':
        nombre_curso = request.POST['curso']
        numero_camada = int(request.POST['camada'])

        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()

    return render(request,"appcoder/curso_formulario.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def creacion_profesores(request):

    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST)

        #validamos que el formulario no tenga problemas
        if formulario.is_valid():

            #recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])
            profesor.save()
        
        return render(request, "appcoder/index.html")
    
    else:
        formulario = ProfesorFormulario()

    contexto = {"formulario":formulario}

    return render(request, "appcoder/profesores_formularios.html", contexto)

def buscar_curso(request):
    return render(request, "appcoder/busqueda_cursos.html")

def resultados_busqueda_cursos(request):

    return render(request, "appcoder/resultados_busquedas_cursos.html")
    pass

def entregables(request):
    return render(request, "appcoder/entregables.html")

#def listado_cursos(request):
#    cursos = Curso.objects.all()

#    cadena_respuesta = ""
#    for curso in cursos:
#        cadena_respuesta += curso.nombre + " | "
    
#    return HttpResponse(cadena_respuesta)
