from django.db import models

from account.models import User

class Worker(models.Model):
    cpf = models.CharField(max_length=14,unique=True,blank=False,primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    contratacao = models.DateField()
    cargo = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + " " + self.sobrenome

