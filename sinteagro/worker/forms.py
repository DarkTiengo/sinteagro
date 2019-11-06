from django import forms

from .models import Worker

MONTHS = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

AREA_SELECT = [
    ("ADM","Administração"),
    ("PROD","Produção"),
    ("MAN","Manutenção")
]

STATUS = [(0,"Ativo"),(1,"Desativado")]

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('cpf','nome','sobrenome','contratacao','area','cargo','pagamento','status','user')
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
            'contratacao': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'area': forms.Select(attrs={'class': 'form-control'},choices=AREA_SELECT),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'pagamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={"class":"form-control"},choices=STATUS),
            'user': forms.HiddenInput()
        }