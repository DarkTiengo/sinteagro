from django.db import models

from account.models import User

class Fazenda(models.Model):
    """Cadastro da fazenda do Usuario. / Farm registrarion"""
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=200)
    tipo = models.IntegerField(default=0)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna o nome da fazenda quando o objeto e chamado / Return Farm Name"""
        return self.nome

class Talhao(models.Model):
    """Cadastro de talhoes / Field Registration"""
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fazenda = models.ForeignKey(Fazenda,on_delete= models.CASCADE)
    nome = models.CharField(max_length=100, null=False)
    tamanho = models.IntegerField(default=0)
    tipo = models.CharField(max_length=1,default=1)
    produto = models.CharField(max_length=10,default="Soja")
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Talhoes"

    def __str__(self):
        """Retorna o nome do talhao quando o objeto e chamado / Return Field Name"""
        return self.nome

class Safra(models.Model):
    """Cadastro de Safras / Crops Registration"""
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ano1 = models.CharField(max_length=4)
    ano2 = models.CharField(max_length=4)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna a safra / Return Crop"""
        return self.ano1 + "/" + self.ano2

class Produtividade(models.Model):
    """Cadastro de produtividades de talhoes / """
    talhao = models.ForeignKey(Talhao,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    safra = models.ForeignKey(Safra,on_delete=models.CASCADE,blank=False)
    producao = models.FloatField(max_length=4,blank=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """"Retorna a producao"""
        return self.producao

class Analise(models.Model):
    """Cadastro da Analise de Solo"""
    safra = models.ForeignKey(Safra,on_delete=models.CASCADE)
    talhao = models.ForeignKey(Talhao,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    N = models.FloatField()
    P = models.FloatField()
    K = models.FloatField()
    S = models.FloatField()
    Ca = models.FloatField()
    Mg = models.FloatField()
    Al = models.FloatField()
    MO = models.FloatField()
    Mn = models.FloatField()
    Zn = models.FloatField()
    Cu = models.FloatField()
    Fe = models.FloatField()
    B = models.FloatField()
    SO4 = models.FloatField()
    pH = models.FloatField()
