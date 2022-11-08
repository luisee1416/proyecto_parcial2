from django.db import models
from model_utils import Choices
from django.core.validators import *
from django.contrib.auth.models import User

from apps.usuario.forms import *

   
# class TipoPlato(models.Model):
#     ENTRADA = 'EN'
#     PLATO_PRINICPAL = 'PR'
#     POSTRE = 'PO'
#     DESCRIPCION = [
#         (ENTRADA, 'ENTRADA'),
#         (PLATO_PRINICPAL, 'PLATO_PRINICPAL'),
#         (POSTRE, 'POSTRE'),

#     ]
  
#     descripcion = models.CharField(max_length=2, choices=DESCRIPCION)
#     activo = models.BooleanField(default=True)
   
   
class Tipo_Plato(models.Model):
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
   
   
   
   

class Vianda(models.Model):
    NORMAL = 'N'
    VEGETARIANO = 'V'
    CELIACO = 'C'
    DIABETICO = 'D'
    TIPO_PLATO = [
        (NORMAL, 'NORMAL'),
        (VEGETARIANO, 'VEGETARIANO'),
        (CELIACO, 'CELIACO'),
        (DIABETICO, 'DIABETICO')
    ]
    
    QUINCENAL = 'Q'
    MENSUAL = 'M'
    FRECUENCIA = [
        (QUINCENAL, 'QUINCENAL'),
        (MENSUAL, 'MENSUAL'),

    ]
    
    PENDIENTE = 'PE'
    CONFIRMADO = 'CO'
    CANCELADO = 'CA'
    
    ESTADO = [
        (PENDIENTE, 'PENDIENTE'),
        (CONFIRMADO, 'CONFIRMADO'),
        (CANCELADO, 'CANCELADO'),
        
    ]
    
    frecuencia = models.CharField(max_length=2, choices=FRECUENCIA)
    fecha_inicio = models.DateField()
   # cantidad = models.IntegerField(min_value=1)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    estado = models.CharField(max_length=10, choices=ESTADO,default="PENDIENTE")
    #tipo_plato = models.ForeignKey(Tipo_Plato, on_delete=models.PROTECT)
    tipo_plato = models.ManyToManyField(Tipo_Plato)
    vigente = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
   
   
   
    def __str__(self):
        return "%s %s %s %s %s" % (self.frecuencia, self.fecha_inicio, self.cantidad, self.tipo_plato, self.usuario)

   #user.username
   
   
