from django.db import models
import uuid

# Create your models here.


class Productos(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name="ID_producto")
    name = models.CharField(max_length=50, verbose_name="Nombre_Producto")
    cantidad = models.IntegerField()
    lote = models.IntegerField()
    stock = models.CharField(max_length=30)
    precio = models.IntegerField()
    fecha = models.DateField()
    marca = models.CharField(max_length=50)
    

    def __str__(self) -> str:
        return f"{self.name}"

#class ControlProductos(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID_registro", editable=False)
    #id_producto = models.ForeignKey(
        #Productos, on_delete=models.CASCADE , verbose_name="ID_producto"
    #)
    #fecha = models.DateField()
    #estado = models.BooleanField()
    #comentarios = models.TextField()
    