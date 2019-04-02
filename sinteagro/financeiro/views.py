from django.shortcuts import render
import datetime

def extrato(request):
    now = datetime.datetime.now()
    meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
    contexto = {'month': meses,'now': meses[now.month-1]}
    return render(request,"financeiro/extrato.html",contexto)

def account(request):
    return render(request,"financeiro/conta.html",)