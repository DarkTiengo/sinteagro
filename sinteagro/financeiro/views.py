from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import datetime

from .forms import ContaForm, ExtratoForm,AutoExtratoForm
from .classes import *

@login_required
def set_extrato(request):
    if request.method == "POST":
        form = AutoExtratoForm(request.FILES)
        if form.is_valid:
            account = request.POST.get("conta")
            ex = Extrato_Reader(request.FILES["file"],request.user,account)
            if ex.is_valid():
                ex.save_extrato()
                data = {"message": "Extrato cadastrado com sucesso!", "type": "alert-success"}
            else:
                data = {"message": "Erro!", "type": "alert-danger"}
            return JsonResponse(data)
    else:
        return render(request,"financeiro/autofile.html",context={"view_set": "set_extrato"})

@login_required
def get_extrato(request):
    resultado = class_extrato(request)
    return JsonResponse(resultado)

@login_required
def set_auto_conta(request):
    if request.method == "POST":
        form = AutoExtratoForm(request.FILES)
        if form.is_valid:
            ex = Extrato_Reader(request.FILES["file"],request.user)
            if ex is not False:
                return JsonResponse(ex.account_auto_create())
        return JsonResponse({"type": "alert-error", "message": "Problemas ao criar a conta, cheque o arquivo e tente novamente."})
    else:
        return render(request, "financeiro/autofile.html",context={"view_set": "set_auto_conta"})

@login_required
def extrato(request):
    """Show Informations of Account's Bank"""
    now = datetime.datetime.now()
    year = (range(2010,now.year+1,+1))
    bancos = get_bancos_user(request)
    contas = class_accounts(request, bancos[0])
    saldo_extrato = str(get_saldo(request,mes=now.month,ano=now.year)).replace('.',',')
    meses = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}
    contexto = {'month': meses,'now': now.month,'info': bancos,'year': year,'now_year': now.year,'cc_number': len(contas),'accounts': contas,'saldo': saldo_extrato}
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
    return class_user_bank(request=request)

@login_required
def get_accounts(request):
        banco = request.GET.get('banco')
        data = class_accounts(request,banco)
        result = {"agencia": [],"conta": []}
        for ag, cc in data:
            result["agencia"].append(ag)
            result["conta"].append(cc)
        return JsonResponse(result)

@login_required
def lancamento(request):
    if request.is_ajax:
        form = ExtratoForm()
        return render(request,"financeiro/lancamento.html",{'form': form})
    if request.method == "POST":
        contexto = {"teste": "ok"}
        return JsonResponse(contexto)

@login_required
def saldo(request):
    if request.method == "POST":
        return JsonResponse({'data': set_saldo(request)})
    else:
        ano = request.GET['ano']
        mes = request.GET['mes']
        return JsonResponse({'data': get_saldo(request,ano,mes)})


