from django.forms import ModelForm,Select,TextInput

from .models import Conta,banco_choices

class ContaForm(ModelForm):
    class Meta:
        model = Conta
        fields = ['banco','agencia','conta']
        widgets ={
            'banco': Select(attrs={'class': 'form-control'},choices=banco_choices),
            'agencia': TextInput(attrs={'class': 'form-control','type': 'number'}),
            'conta': TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }