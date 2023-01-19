from django.shortcuts import render, redirect

from .carrito import Carrito
from .models import Disco
# Create your views here.


def index(request):
    discos = Disco.objects.all()
    cantidad = 0
    if request.session.get('carrito'):
        cantidad = len(request.session.get('carrito'))
    return render(request, 'index.html', {"discos": discos, "cantidad_discos": cantidad})


def agregar_disco(request, disco_id):
    carrito = Carrito(request)
    disco = Disco.objects.get(id=disco_id)
    carrito.agregar(disco)
    return redirect(index)


def eliminar_disco(request, disco_id):
    carrito = Carrito(request)
    disco = Disco.objects.get(id=disco_id)
    carrito.eliminar(disco)


def restar_disco(request, disco_id):
    carrito = Carrito(request)
    disco = Disco.objects.get(id=disco_id)
    carrito.restar(disco)
    return redirect(index)


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(index)


def carritoCompra(request):
    discos = Disco.objects.all()
    cantidad = 0
    if request.session.get('carrito'):
        cantidad = len(request.session.get('carrito'))
    return render(request, 'carrito.html', {"discos": discos, "cantidad_discos": cantidad})


def agregar_disco_carrito(request, disco_id):
    carrito = Carrito(request)
    disco = Disco.objects.get(id=disco_id)
    carrito.agregar(disco)
    return redirect(carritoCompra)


def restar_disco_carrito(request, disco_id):
    carrito = Carrito(request)
    disco = Disco.objects.get(id=disco_id)
    carrito.restar(disco)
    return redirect(carritoCompra)


def limpiar_disco_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(carritoCompra)


def comprar(request):
    carrito = Carrito(request)
    print()
    if request.session['carrito']:
        for key, value in request.session["carrito"].items():
            disco = Disco.objects.get(id=value['disco_id'])
            if disco.stock >= 1:
                disco.stock -= value["cantidad"]
                disco.save()
        carrito.limpiar()
        return render(request,'compra.html')
    return redirect(carritoCompra)



