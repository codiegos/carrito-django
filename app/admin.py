from django.contrib import admin
from .models import Disco
# Register your models here.

class DiscoAdmin(admin.ModelAdmin):
  list_display = ['codigo','nombre','descripcion','valor','url_imagen','tipoDisco']

admin.site.register(Disco,DiscoAdmin)