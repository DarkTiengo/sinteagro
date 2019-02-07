from django import forms

from .models import Fazenda,Talhao,Safra,Produtividade

class FazendaForm(forms.ModelForm):
    class Meta:
        model = Fazenda
        fields = ['nome','estado','cidade','tipo']
        labels = {'nome': 'Nome da Fazenda','estado': 'Estado','cidade': 'Cidade','tipo' : 'Tipo'}

class TalhaoForm(forms.ModelForm):
    class Meta:
        model = Talhao
        fields = ['fazenda','nome','tamanho','tipo','produto']
        labes = {'nome': 'Nome do Talhao', 'tamanho': 'Tamanho do Talhao','tipo': 'Tipo de negocio','produto': 'Produto'}

class SafraForm(forms.ModelForm):
    class Meta:
        model = Safra
        fields = ['ano1', 'ano2']
        labels = {"ano1": "Ano", "ano2": "Ano"}

class ProdutividadeForm(forms.ModelForm):
    class Meta:
        model = Produtividade
        fields = ['safra','producao','talhao']
        labels = {'safra': 'Safra', 'producao': 'Producao', 'talhao': 'Talhao'}