from django import forms

from .models import Conta

banco_choices =  (
    ("001","Banco do Brasil"),
    ("999", "Outros Bancos")
)

class ContaForm(forms.Form):
    banco = forms.CharField(
        max_length=3,
        widget=forms.Select(attrs={'class': 'form-control'},choices=banco_choices)
    )
    agencia = forms.CharField(max_length=10,
                              widget=forms.NumberInput({'class': 'form-control account'})
                              )
    conta = forms.CharField(max_length=10,
                              widget=forms.NumberInput({'class': 'form-control account'})
                            )

    def clean(self):
        cleaned_data = super(ContaForm,self).clean()
        banco = cleaned_data.get('banco')
        agencia = cleaned_data.get('agencia')
        conta = cleaned_data.get('conta')
        if not banco and not agencia and not conta:
            raise forms.ValidationError("Preencha os dados corretamente")