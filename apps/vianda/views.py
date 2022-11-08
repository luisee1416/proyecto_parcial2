from django.shortcuts import render
from apps.vianda.forms import nuevaViandaForm

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.vianda.models import Vianda










from .forms import nuevaViandaForm
from .models import Vianda
# Create your views here.


def listar_viandas(request):
    return render(request, 'vianda/listar_viandas.html', {'viandas': Vianda.objects.filter(usuario=request.user)})


def creacion_vianda(request):

    if (request.method == "POST"):
        # se crea instancia de vianda,usando los datos de request.post
        vianda = nuevaViandaForm(request.POST)
        if (vianda.is_valid()):
            nueva_vianda = vianda.save(commit=False)
            nueva_vianda.usuario = request.user
            nueva_vianda.save()

            messages.success(request, 'Se ha agregado correctamente la Vianda {}'.format(
                nueva_vianda))
            return redirect('vianda:creacion_vianda')
    else:
        vianda = nuevaViandaForm()

    return render(request, 'vianda/crearVianda.html', {'vianda': vianda})
