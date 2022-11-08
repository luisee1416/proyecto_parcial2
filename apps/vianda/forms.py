
from django import forms

from apps.vianda.models import Vianda


class nuevaViandaForm(forms.ModelForm):
    class Meta:
        model = Vianda

        fields = (
            "frecuencia", "fecha_inicio", "cantidad", "estado", "tipo_plato", "vigente", "usuario")

        widgets = {

            'fecha_inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),

        }
        