from django.db import models
# Create your models here.
class TipoDisco(models.Model):
  nombre = models.CharField(max_length=30)
  def __str__(self) -> str:
    return self.nombre

class Disco(models.Model):
  codigo = models.CharField(max_length=30)
  nombre = models.CharField(max_length=30)
  descripcion = models.CharField(max_length=200)
  valor = models.IntegerField()
  url_imagen = models.URLField(max_length=200)
  stock = models.IntegerField(default=10)
  tipoDisco = models.ForeignKey(TipoDisco, on_delete=models.CASCADE)

class TipoUsuario(models.Model):
  nombre = models.CharField(max_length=30)

  def __str__(self) -> str:
    return self.nombre
  
class Usuario(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  fecha_nacimiento = models.DateField()
  tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)


  