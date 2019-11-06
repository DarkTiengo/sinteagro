from django.db import models
from django.forms import ModelForm

from account.models import User

class Worker(models.Model):
    cpf = models.CharField(max_length=14,unique=True,blank=False,primary_key=True,verbose_name='CPF')
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    contratacao = models.DateField(verbose_name='Data de Contratação')
    area = models.CharField(max_length=50,verbose_name='Area de atuação')
    cargo = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    pagamento = models.IntegerField(default=0,verbose_name='Dia limite de pagamento',help_text='Dia combinado para pagamento de salário')
    atualizacao = models.DateField(auto_now_add=True)

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['cpf','nome','sobrenome','contratacao','area','cargo','status','pagamento']