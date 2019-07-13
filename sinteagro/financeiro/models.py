from django.db import models
import datetime

from account.models import User

class Conta(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    banco = models.CharField(max_length=20)
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Contas Bancárias"
        verbose_name = "Conta Bancária"

    def __str__(self):
        return "Ag: " + self.agencia + "/" + "CC " + self.conta

class Extrato(models.Model):
    conta = models.ForeignKey(Conta,on_delete=models.CASCADE)
    operacao = models.IntegerField()
    date = models.DateField(default=datetime.datetime.now)
    history = models.CharField(max_length=30)
    obs = models.CharField(max_length=30,blank=True)
    valor = models.FloatField(max_length=10)
    type = models.CharField(max_length=10,default="null")
    document = models.CharField(max_length=50,default=0)

    class Meta:
        verbose_name = "Extrato Bancário"
        verbose_name_plural = "Extratos Bancários"

    def __str__(self):
        return self.date + " = " + self.valor

class Saldo_Inicial(models.Model):
    conta = models.ForeignKey(Conta,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mes = models.PositiveSmallIntegerField()
    ano = models.PositiveIntegerField()
    saldo = models.FloatField()

    class Meta:
        verbose_name_plural = "Extratos Bancários"
        verbose_name = "Extrato Bancário"

    def __str__(self):
        return self.mes + "/" + self.ano + " = " + self.saldo