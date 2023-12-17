from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 200)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre