from django.urls import path
from . import views
from apps.usuario import views

from .views import Vianda, creacion_vianda,listar_viandas



app_name = 'vianda'
urlpatterns = [
    path("creacion_vianda/", creacion_vianda, name="creacion_vianda"),  
    path("listar_viandas/",listar_viandas, name="listar_viandas"), 
     
 ]
