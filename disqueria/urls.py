"""disqueria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.authViews.views import discos, agregarDisco, actualizarDisco, eliminarDisco, tipoDiscos, agregarTipoDisco, actualizarTipoDisco, eliminarTipoDisco, usuarios, tipoUsuarios, agregarUsuario, actualizarUsuario, eliminarUsuario, agregarTipoUsuario, actualizarTipoUsuario, eliminarTipoUsuario
from app.views import index, carritoCompra, agregar_disco, eliminar_disco, limpiar_carrito, restar_disco,agregar_disco_carrito,limpiar_disco_carrito,restar_disco_carrito,comprar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('dashboard/', discos, name='dashboard'),
    path('agregarDisco/', agregarDisco, name='agregarDisco'),
    path('actualizarDisco/<int:id>',actualizarDisco, name='actualizarDisco'),
    path('eliminarDisco/<int:id>',eliminarDisco, name='eliminarDisco'),

    path('tiposDiscos/', tipoDiscos, name='tipoDiscos'),
    path('agregarTipoDisco/', agregarTipoDisco, name='agregarTipoDisco'),
    path('actualizarTipoDisco/<int:id>',actualizarTipoDisco, name='actualizarTipoDisco'),
    path('eliminarTipoDisco/<int:id>',eliminarTipoDisco, name='eliminarTipoDisco'),

    path('usuarios/', usuarios, name='usuarios'),
    path('agregarUsuario/', agregarUsuario, name='agregarUsuario'),
    path('actualizarUsuario/<int:id>', actualizarUsuario, name='actualizarUsuario'),
    path('eliminarUsuario/<int:id>', eliminarUsuario, name='eliminarUsuario'),

    path('tipoUsuarios/', tipoUsuarios, name='tipoUsuarios'),
    path('agregarTipoUsuario/', agregarTipoUsuario, name='agregarTipoUsuario'),
    path('actualizarTipoUsuario/<int:id>',actualizarTipoUsuario, name='actualizarTipoUsuario'),
    path('eliminarTipoUsuario/<int:id>',eliminarTipoUsuario, name='eliminarTipoUsuario'),


    path('', index),
    path('agregar/<int:disco_id>', agregar_disco, name='Add'),
    path('restar/<int:disco_id>', restar_disco, name='Sub'),
    path('limpiar/', limpiar_carrito, name='CLS'),

    path('eliminar/<int:disco_id>', eliminar_disco, name='Del'),

    path('carrito/', carritoCompra, name='carrito'),
    path('agregar_disco_carrito/<int:disco_id>', agregar_disco_carrito, name='AddCarrito'),
    path('restar_disco_carrito/<int:disco_id>', restar_disco_carrito, name='SubCarrito'),
    path('limpiar_disco_carrito/', limpiar_disco_carrito, name='cleanCarrito'),

    path('compraExitosa/', comprar, name='comprar'),

]
