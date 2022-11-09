from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.
# makemigrations
# migrate

#CREANDO CLASE CLIENTE
class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=True)
    correo = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

#CREANDO CLASE CATEGORIA
class Categoria(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre

#CREANDO CLASE PRODUCTOS
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.nombre
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ' '
        return url
