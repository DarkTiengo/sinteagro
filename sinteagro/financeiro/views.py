from django.shortcuts import render
from django.http import JsonResponse
import datetime

from .forms import ContaForm

def extrato(request):
    now = datetime.datetime.now()
    meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
    contexto = {'month': meses,'now': meses[now.month-1]}
    return render(request,"financeiro/extrato.html",contexto)

def account(request):
    if request.method == "POST":
        form = ContaForm(request.POST)
        if form.is_valid():
            form.save()
            contexto = {
                "type": "alert-success",
                "message": "Conta registrada com sucesso!"
            }
            return JsonResponse(contexto)
        else:
            contexto = {
                "type": "alert-danger",
                "message": "Ocorreu um problema, por favor tente novamente."
            }
            return JsonResponse(contexto)
    else:
        form = ContaForm()
        return render(request,"financeiro/conta.html",{'form': form})