from django.forms import ModelForm,Select,TextInput,Textarea,HiddenInput
from django import forms

from .models import Conta,Extrato

class AutoExtratoForm(forms.Form):
    file = forms.FileField()

class ContaForm(ModelForm):
    class Meta:
        model = Conta
        fields = ['banco','agencia','conta']
        widgets ={
            'banco': Select(attrs={'class': 'form-control'}),
            'agencia': TextInput(attrs={'class': 'form-control','type': 'number','placeholder': 'Somente números','id': 'agencia'}),
            'conta': TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Somente números','id': 'conta'}),
        }

class ExtratoForm(ModelForm):
    class Meta:
        model = Extrato
        fields = ['obs','valor','date','history','operacao']
        widgets = {
            'obs': Textarea(attrs={
                'class': 'form-control',
                'maxlength': 30,
                'rows': 2,
                'cols': 6,
            }),
            'valor': TextInput({
                'class': 'form-control',
                'maxlenght': 30,
                'type': 'text',
                'id': 'valor',
            }),
            'date': TextInput({
                'class': 'form-control',
                'type': 'date',
            }),
            'history': TextInput(attrs={
               'class': 'form-control',
                'maxlength': 30,
            }),
            'operacao': HiddenInput()
        }