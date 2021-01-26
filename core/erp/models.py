from django.db import models
from django.db.models import Model 
from datetime import datetime
from PIL import Image
#import pillow 



# Create your models here.

class Trabajador(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    rut = models.CharField(max_length=10, unique=True, verbose_name="rut")
    fecha_registro = models.DateField(default=datetime.now, verbose_name="Fecha de Registro")
    fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=False)
    fecha_actualizacion = models.DateTimeField(auto_now=False, auto_now_add=False)
    age = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default= 0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="avatar/%d/%m/%Y", null=True, blank=True)
    curriculum = models.FileField(upload_to="cvitae/%d/%m/%Y", max_length = 100, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'Trabajador'
        managed = True
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ['id']       # ordering = [-id]  descendente

    
