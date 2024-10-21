from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
