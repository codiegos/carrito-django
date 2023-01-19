from django.shortcuts import render, redirect

from ..views import index
from ..models import Disco,TipoDisco,Usuario,TipoUsuario
from ..forms import UsuarioForm,TipoUsuarioForm,DiscoForm,TipoDiscoForm
# Create your views here.

def discos(request):
  if request.user.is_authenticated:
    discos = Disco.objects.all()
    return render(request, 'auth/discos.html', {"discos": discos})
  return redirect(index)

def agregarDisco(request):
  if request.user.is_authenticated:
    form = DiscoForm()
    if request.method == "POST":
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save() 
            return discos(request)
    return render(request, 'auth/upsertDisco.html', {"form": form})
  return redirect(index)

def actualizarDisco(request,id):
  if request.user.is_authenticated:
    disco = Disco.objects.get(id=id)
    form = DiscoForm(instance=disco)
    if request.method == "POST":
        form = DiscoForm(request.POST,instance=disco)
        if form.is_valid():
            form.save()
        return discos(request)
    return render(request, 'auth/upsertDisco.html', {"form": form})
  return redirect(index)

def eliminarDisco(request,id):
  if request.user.is_authenticated:
    disco = Disco.objects.get(id=id)
    disco.delete()
    return discos(request)
  return redirect(index)
    
def tipoDiscos(request):
  if request.user.is_authenticated:
    tipoDiscos = TipoDisco.objects.all()
    return render(request, 'auth/tipoDiscos.html', {"tipoDiscos": tipoDiscos})
  return redirect(index)

def agregarTipoDisco(request):
  if request.user.is_authenticated:
    form = TipoDiscoForm()
    if request.method == "POST":
        form = TipoDiscoForm(request.POST)
        if form.is_valid():
            form.save() 
            return tipoDiscos(request)
    return render(request, 'auth/upsertDisco.html', {"form": form})
  return redirect(index)

def actualizarTipoDisco(request,id):
  if request.user.is_authenticated:
    tipoDisco = TipoDisco.objects.get(id=id)
    form = TipoDiscoForm(instance=tipoDisco)
    if request.method == "POST":
        form = TipoDiscoForm(request.POST,instance=tipoDisco)
        if form.is_valid():
            form.save()
        return tipoDiscos(request)
    return render(request, 'auth/upsertDisco.html', {"form": form})
  return redirect(index)


def eliminarTipoDisco(request,id):
  if request.user.is_authenticated:
    tipoDisco = TipoDisco.objects.get(id=id)
    tipoDisco.delete()
    return tipoDiscos(request)
  return redirect(index)


def usuarios(request):
  if request.user.is_authenticated:
    usuarios = Usuario.objects.all()
    return render(request, 'auth/usuarios.html', {"usuarios": usuarios})
  return redirect(index)

def agregarUsuario(request):
  if request.user.is_authenticated:
    form = UsuarioForm()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save() 
            return usuarios(request)
    return render(request, 'auth/upsertUsuario.html', {"form": form})
  return redirect(index)

def actualizarUsuario(request,id):
  if request.user.is_authenticated:
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(instance=usuario)
    if request.method == "POST":
        form = UsuarioForm(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
        return usuarios(request)
    return render(request, 'auth/upsertUsuario.html', {"form": form})
  return redirect(index)

def eliminarUsuario(request,id):
  if request.user.is_authenticated:
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return usuarios(request)
  return redirect(index)


def tipoUsuarios(request):
  if request.user.is_authenticated:
    tipoUsuarios = TipoUsuario.objects.all()
    return render(request, 'auth/tipoUsuarios.html', {"tipoUsuarios": tipoUsuarios})
  return redirect(index)

def agregarTipoUsuario(request):
  if request.user.is_authenticated:
    form = TipoUsuarioForm()
    if request.method == "POST":
        form = TipoUsuarioForm(request.POST)
        if form.is_valid():
            form.save() 
            return tipoUsuarios(request)
    return render(request, 'auth/upsertUsuario.html', {"form": form})
  return redirect(index)

def actualizarTipoUsuario(request,id):
  if request.user.is_authenticated:
    tipoUsuario = TipoUsuario.objects.get(id=id)
    form = TipoUsuarioForm(instance=tipoUsuario)
    if request.method == "POST":
        form = TipoUsuarioForm(request.POST,instance=tipoUsuario)
        if form.is_valid():
            form.save()
        return tipoUsuarios(request)
    return render(request, 'auth/upsertUsuario.html', {"form": form})
  return redirect(index)

def eliminarTipoUsuario(request,id):
  if request.user.is_authenticated:
    tipoUsuario = TipoUsuario.objects.get(id=id)
    tipoUsuario.delete()
    return redirect(tipoUsuarios)
  return redirect(index)
  