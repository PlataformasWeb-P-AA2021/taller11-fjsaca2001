from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# Create your views here.

# importar las clases de models.py
from administrativo.models import Edificio, Departamento

# importar los formularios de forms.py
from administrativo.forms import EdificioForm, DepartamentoForm, DepartamentoEdificioForm


# Create your views here.

def index(request):
    """
    Listar los Edificios y departamentos de la base de datos
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # edificios
    edificio = Edificio.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'edificios': edificio, 'numero_edificios': len(edificio)}
    return render(request, 'index.html', informacion_template)


def verEdificio(request, id):
    """
         Listar los registros del modelo Estudiante,
         obtenidos de la base de datos.
     """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    edificio = Edificio.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'edificio': edificio}
    return render(request, 'listarEdificio.html', informacion_template)


def crearEdificio(request):
    """
    """
    if request.method == 'POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()  # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEdificio.html', diccionario)


def editarEdificio(request, id):
    """
        """
    edificio = Edificio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)


def eliminarEdificio(request, id):
    """
        """
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)


def crearDepartamento(request):
    """
    """
    if request.method == 'POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()  # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearDepartamento.html', diccionario)


def editarDepartamento(request, id):
    """
        """
    departamento = Departamento.objects.get(pk=id)
    if request.method == 'POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editarDepartamento.html', diccionario)


def agregarDepartamentoEdificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = DepartamentoEdificioForm(edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}

    return render(request, 'crearDepartamentoEdificio.html', diccionario)
