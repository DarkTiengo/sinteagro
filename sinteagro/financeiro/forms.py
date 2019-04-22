from django.forms import ModelForm,Select,TextInput,Textarea

from .models import Conta,banco_choices,Extrato

class ContaForm(ModelForm):
    class Meta:
        model = Conta
        fields = ['banco','agencia','conta']
        widgets ={
            'banco': Select(attrs={'class': 'form-control'},choices=banco_choices),
            'agencia': TextInput(attrs={'class': 'form-control','type': 'number'}),
            'conta': TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }

class ExtratoForm(ModelForm):
    class Meta:
        model = Extrato
        fields = ['obs','valor','date','history']
        widgets = {
            'obs': Textarea(attrs={
                'class': 'form-control',
                'maxlength': 30,
            }),
            'valor': TextInput({
                'class': 'form-control',
                'maxlenght': 30,
                'type': 'number',
            }),
            'date': TextInput({
                'class': 'form-control',
                'type': 'date',
            }),
            'history': Textarea(attrs={
               'class': 'form-control',
                'maxlength': 30
            }),
        }