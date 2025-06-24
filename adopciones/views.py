from django.shortcuts import render, redirect, get_object_or_404
from .models import Perro, UsuarioAdoptante, RAZAS, TAMAÑOS, SALUD, TEMPERAMENTOS, ESTADOS
from .forms import UsuarioAdoptanteForm, PerroForm, BuscarPerroForm

#Vista usuario adoptante
def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioAdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perros')
    else:
        form = UsuarioAdoptanteForm()
        print(form.errors)
    return render(request, 'registrar_usuario.html', {'form': form})

#Vista perros
def registrar_perro(request):
    if request.method == 'POST':
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perros')
    else:
        form = PerroForm()
        print(form.errors)
    return render(request, 'registrar_perro.html', {'form': form})

def lista_perros(request):
    perros = Perro.objects.all()
    form = BuscarPerroForm(request.GET or None)

    if form.is_valid():
        raza = form.cleaned_data.get('raza')
        edad = form.cleaned_data.get('edad')
        tamaño = form.cleaned_data.get('tamaño')
        estado = request.GET.get('estado')

        if raza:
            perros = perros.filter(raza__iexact=raza)
        if edad:
            perros = perros.filter(edad=edad)
        if tamaño:
            perros = perros.filter(tamaño__iexact=tamaño)
        if estado:
            perros = perros.filter(estado=estado)


    return render(request, 'lista_perros_v2.html', {'perros': perros, 'RAZAS': RAZAS,
        'TAMAÑOS': TAMAÑOS, 'ESTADOS': ESTADOS}) #v2
    # return render(request, 'lista_perros_v2.html', {'perros': perros})

def lista_perros_v1(request):
    perros = Perro.objects.all()
    form = BuscarPerroForm(request.GET or None)

    if form.is_valid():
        raza = form.cleaned_data.get('raza')
        edad = form.cleaned_data.get('edad')
        tamaño = form.cleaned_data.get('tamaño')
        

        if raza:
            perros = perros.filter(raza__iexact=raza)
        if edad:
            perros = perros.filter(edad=edad)
        if tamaño:
            perros = perros.filter(tamaño__iexact=tamaño)




    return render(request, 'lista_perros.html', {'perros': perros}) #v2


def buscar_para_usuario(request):
    perros = None
    usuario = None
    busqueda_realizada = False
    if request.method == 'POST':
        dni = request.POST.get('dni')
        try:
            usuario = UsuarioAdoptante.objects.get(dni=dni)
        except UsuarioAdoptante.DoesNotExist:
            return render(request, 'buscar_para_usuario.html', {'error': 'Usuario no encontrado'})

        perros = Perro.objects.filter(estado='disponible')

        if usuario.preferencias_raza:
            perros = perros.filter(raza__iexact=usuario.preferencias_raza)
        if usuario.preferencias_edad:
            perros = perros.filter(edad=usuario.preferencias_edad)
        if usuario.preferencias_tamaño:
            perros = perros.filter(tamaño__iexact=usuario.preferencias_tamaño)

        busqueda_realizada = True

    return render(request, 'buscar_para_usuario.html',{'perros': perros, 'usuario': usuario, 'busqueda_realizada': busqueda_realizada})


def postular_adopcion(request, id_perro, dni_usuario):
    perro = get_object_or_404(Perro, id=id_perro)
    usuario = get_object_or_404(UsuarioAdoptante, dni=dni_usuario)

    if perro.estado == 'disponible':
        perro.estado = 'reservado'
        perro.reservado_por = usuario
        perro.save()
        mensaje = f"{usuario.nombre} postuló la adopción de {perro.nombre}."
    else:
        mensaje = "El perro ya no está disponible."

    # Luego de postular, podrías volver al mismo listado:
    perros = Perro.objects.filter(estado='disponible')

    # Aplicar nuevamente el filtrado de preferencias:
    if usuario.preferencias_raza:
        perros = perros.filter(raza__iexact=usuario.preferencias_raza)
    if usuario.preferencias_edad:
        perros = perros.filter(edad=usuario.preferencias_edad)
    if usuario.preferencias_tamaño:
        perros = perros.filter(tamaño__iexact=usuario.preferencias_tamaño)

    return render(request, 'buscar_para_usuario.html', {'perros': perros, 'usuario': usuario, 'mensaje': mensaje})

def confirmar_adopcion(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        try:
            usuario = UsuarioAdoptante.objects.get(dni=dni)
        except UsuarioAdoptante.DoesNotExist:
            return render(request, 'confirmar_adopcion.html', {'error': 'Usuario no encontrado'})

        perros_reservados = Perro.objects.filter(estado='reservado',reservado_por=usuario)

        if 'confirmar' in request.POST:
            id_perro = request.POST.get('confirmar')
            perro = Perro.objects.get(id=id_perro)
            perro.estado = 'adoptado'
            perro.save()
            mensaje = f"El perro {perro.nombre} fue adoptado por {usuario.nombre}."

            perros_reservados = Perro.objects.filter(estado='reservado',reservado_por=usuario)

            return render(request, 'confirmar_adopcion.html', {'usuario': usuario, 'perros': perros_reservados, 'mensaje': mensaje})

        return render(request, 'confirmar_adopcion.html', {'usuario': usuario, 'perros': perros_reservados})

    return render(request, 'confirmar_adopcion.html')