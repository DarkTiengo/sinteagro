from django.db import models

from account.models import User

class Conta(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    banco = models.CharField(max_length=3,default="001")
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Contas Bancárias"
        verbose_name = "Conta Bancária"

    def __str__(self):
        return self.conta