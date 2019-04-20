from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import datetime

from .forms import ContaForm
from .models import Conta, banco_choices

@login_required
def extrato(request):
    """Show Informations of Account's Bank"""
    now = datetime.datetime.now()
    meses = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}
    contexto = {'month': meses,'now': now.month,'info': get_bancos_user(request)}
    return contexto

@login_required
def conta(request):
    """Account Form"""
    if request.method == "POST":
        form = ContaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
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

@login_required
def get_bancos_user(request):
    cc = list(Conta.objects.filter(user=request.user).values_list("banco"))
    bancos = dict(banco_choices)
    user_banco = {'Bank': dict()}
    for c in cc:
        for id,b in bancos.items():
            if c[0] == id:
                user_banco['Bank']
                user_banco['Bank'][id] = b
    return user_banco

@login_required
def get_accounts(request):
    if request.is_ajax:
        banco = request.GET.get('banco')
        ccs = Conta.objects.filter(banco=banco).values_list('id','agencia','conta')
        result = {'conta': list()}
        for cc in ccs:
            result['conta'].append(cc)
        return JsonResponse(result)



