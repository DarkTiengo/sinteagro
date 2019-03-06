from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime

from .forms import FazendaForm, TalhaoForm, SafraForm, ProdutividadeForm, AgendaForm
from .fazendas import *
from .talhoes import *
from account.auxiliar import *
from account.forms import UserForm
from .models import Agenda


@login_required()
def index(request):
    """Pagina inicial  / Main Menu"""
    contexto = gera_Menu(request.user)
    contexto['home'] = True
    contexto['month'] = mes
    contexto['year'] = ano
    return render(request,'sinteagros/index.html',contexto)

@login_required()
def get_events(request):
    """"Get Calendar Events"""
    date = request.GET.get('date')
    month = datetime.strptime(date,'%Y-%m').month
    user = request.user
    try:
        calendar = Agenda.objects.filter(date__month=month,user=user).values()
        result = list(calendar)
    except:
        result = {}
    return JsonResponse(result,safe=False)

def logout(request):
    """Sai do Sistema / Logout"""
    django_logout(request)
    contexto = {"aba" : None, "info": "Voce foi desconectado do sistema."}
    return render(request,'account/login.html',contexto)

#Partes relacionada a Fazenda / Farming Parts
@login_required()
def fazenda(request,fazenda_id,alert = None):
    """Mostra talhoes relacionados a fazenda / Show Farm Fields"""
    contexto = get_fazenda_e_talhoes(fazenda_id=fazenda_id, usuario=request.user)
    if alert is not None:
        contexto['alerta'] = alert
    return render(request,'sinteagros/fazenda.html',contexto)

@login_required()
def cadastrar_fazenda(request):
    """Cadastrar novas fazendas / Create new Farms"""
    contexto = gera_Menu(request.user)
    contexto['cadastro'] = True
    if request.method != 'POST':
        pass
    else:
        form = FazendaForm(request.POST)
        contexto["form"] = form
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            contexto["alerta"] = "erro"
            contexto["mensagem"] = form.errors
    return render(request,'sinteagros/cadastrar_fazenda.html',contexto)

@login_required()
def edit_fazenda(request,fazenda_id):
    """Editar dados da fazenda / Edit Farming's Data"""
    fazenda = get_fazenda(fazenda_id=fazenda_id)
    contexto = gera_Menu(request.user)
    contexto.update(fazenda)
    if request.method == 'POST':
        form = FazendaForm(instance=fazenda['fazenda'],data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('fazenda',args=[fazenda_id,'sucesso']))
        else:
            return HttpResponseRedirect(reverse('fazenda', args=[fazenda_id,'erro']))
    return render(request,'sinteagros/edit_fazenda.html',contexto)

@login_required()
def exclui_fazenda(request,fazenda_id):
    """Exclui fazenda cadastrada / Remove Farming """
    contexto = gera_Menu(request.user)
    fazenda = get_fazenda(fazenda_id=fazenda_id)
    if request.user != fazenda['fazenda'].user:
        raise Http404
    else:
        excluir_fazenda(fazenda_id)
        return render(request,'sinteagros/index.html',contexto)

@login_required()
def talhao(request,fazenda_id,talhao_id, alert = None):
    """Exibe informacoes do talhao / Show Farming Field"""
    contexto = get_fazenda_e_talhoes(fazenda_id=fazenda_id, usuario=request.user)
    contexto.update(get_talhao(talhao_id))
    if alert is not None:
        contexto['alerta'] = alert
    return render(request,'sinteagros/talhao.html',contexto)

@login_required()
def edit_talhoes(request,fazenda_id):
    """"Edita os talhoes / Edit Fields"""
    contexto = get_fazenda_e_talhoes(fazenda_id=fazenda_id, usuario=request.user)
    return render(request,'sinteagros/editar_talhoes.html',contexto)

@login_required()
def cadastrar_talhao(request, fazenda_id):
    """Cadastrar novo talhao / Create New Field"""
    contexto = get_fazenda_e_talhoes(fazenda_id=fazenda_id,usuario=request.user)
    contexto["produto"] = produtos
    if request.method == "POST":
        form = TalhaoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            contexto["info"] = "sucesso"
            contexto["mensagem"] = "Talhao Cadastrado com sucesso."
            return HttpResponseRedirect(reverse('fazenda',args=[contexto["fazenda"].id]))
        else:
            contexto["info"] = "erro"
            contexto["mensagem"] = "Ocorreu um erro, por favor tente novamente."
    return render(request,'sinteagros/cadastrar_talhao.html',contexto)

@login_required()
def edit_talhao(request,fazenda_id,talhao_id = None):
    """"Editar talhao / Edit Field"""
    contexto = get_fazenda_e_talhoes(fazenda_id=fazenda_id,usuario=request.user)
    contexto.update(get_talhao(talhao_id))
    contexto["produto"] = produtos
    if request.method == "POST":
        talhao = get_talhao(request.POST["talhao"])
        dados = TalhaoForm(data=request.POST, instance=talhao["talhao"])
        if dados.is_valid():
            dados.save(commit=False)
            dados.user = request.user
            dados.save()
            return HttpResponseRedirect(reverse('edit_talhoes',args=[fazenda_id]))
        else:
            contexto["info"] = "erro"
            contexto["mensagem"] = "Ocorreu um erro, por favor tente novamente."
        return render(request, 'sinteagros/editar_talhoes.html', contexto)
    return render(request,'sinteagros/cadastrar_talhao.html',contexto)

@login_required()
def apaga_talhao(request,fazenda_id,talhao_id):
    """Remover Talhao / Remove Field"""
    contexto = get_fazenda_e_talhoes(fazenda_id=fazenda_id,usuario=request.user)
    if remove_talhao(talhao_id):
        contexto["info"] = "sucesso"
        contexto["mensagem"] = "Talhao excluido com sucesso."
    else:
        contexto["info"] = "erro"
        contexto["mensagem"] = "Ocorreu um erro, favor tente novamente."
    return HttpResponseRedirect(reverse('edit_talhoes', args=[contexto["fazenda"].id]))

@login_required()
def safra(request):
    """Exibe e cadastra safras / Show and Add new Crop"""
    contexto = gera_Menu(request.user)
    contexto.update(get_safras(request.user))
    return render(request,'sinteagros/safra.html',contexto)

@login_required()
def cadastrar_safra(request):
    """Cadastra Safra / Create New Crop """
    contexto = gera_Menu(request.user)
    ano = 2000
    anos = []
    while ano < 2021:
        anos.append(ano)
        ano += 1
    contexto['anos'] = anos
    if request.method == "POST":
       dados = SafraForm(request.POST)
       if dados.is_valid():
           post = dados.save(commit=False)
           post.user = request.user
           post.save()
           contexto["alerta"] = "sucessso"
           return render(request,'sinteagros/safra.html',contexto)
       else:
           contexto["alerta"] = "erro"
           contexto["mensagem"] = dados.errors
    return render(request,'sinteagros/cadastrar_safra.html',contexto)

@login_required()
def excluir_safra(request):
    """Excluir safra / Remove Crop """
    dados = safra_remove(request.POST["id"])

@login_required()
def configuracoes(request):
    """Exibe e altera informacoes do usuario / Show and edit User Information"""
    contexto = gera_Menu(request.user)
    contexto['profile'] = request.user
    contexto['estados'] = select_estados
    contexto['genero'] = genero
    if request.method == "POST":
        user = UserForm(request.POST,instance=request.user)
        if user.is_valid():
            user.save()
            contexto['info'] = "sucesso"
            contexto['mensagem'] = "Alteracoes feitas com sucesso."
        else:
            contexto['info'] = "erro"
            contexto['mensagem'] = user.errors
    return render(request,'sinteagros/configuracoes.html',contexto)

@login_required()
def altera_senha(request):
    """"Altera senha do usuario / Edit User Password"""
    dados = request.POST
    contexto = gera_Menu(request.user)
    if request.user.check_password(dados["senha"]):
        if dados["novasenha"] == dados["confirmasenha"]:
            request.user.set_password(dados["novasenha"])
            contexto["info"] = "sucesso"
            contexto["mensagem"] = "Senha alterada com sucesso"
        else:
            contexto["info"] = "erro"
            contexto["mensagem"] = "Nova senha nao e igual a confirmacao, favor verificar e tente novamente."
    else:
        contexto["info"] = "erro"
        contexto["mensagem"] = "Senha atual incorreta, favor corrigir e tente novamente."
    return render(request,'sinteagros/configuracoes.html',contexto)

@login_required()
def edit_produtividades(request,fazenda_id,talhao_id):
    """"Gerencia as produtividades / Productivity Manager"""
    contexto = get_fazenda_e_talhoes(fazenda_id=fazenda_id,usuario=request.user)
    contexto.update(get_talhao(talhao_id))
    contexto["produtividades"] = get_produtividade(contexto["talhao"])
    return render(request,'sinteagros/edit_produtividades.html',contexto)

@login_required()
def edit_producao(request,fazenda_id,talhao_id):
    """Edita Produtividade / Edit Productivity"""
    contexto = get_fazenda_e_talhoes(fazenda_id=fazenda_id,usuario=request.user)
    contexto.update(get_talhao(talhao_id))
    contexto.update(get_safras(request.user))
    if request.method == "POST":
        dados = ProdutividadeForm(request.POST)
        if dados.is_valid():
            post = dados.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('edit_produtividades',args=[fazenda_id,talhao_id]))
        else:
            contexto["info"] = "erro"
            contexto["mensagem"] = "Algo deu errado, por favor tente novamente."
    return render(request,"sinteagros/cadastrar_produtividade.html",contexto)

def set_note(request):
    """Manipulate notes / Manipula as notas"""
    if request.method == "POST":
        try:
            date = request.POST.get('date')
            query = Agenda.objects.get(date=date)
            note = AgendaForm(request.POST,instance=query)
        except:
            note = AgendaForm(request.POST)
        if note.is_valid():
            post = note.save(commit=False)
            post.user = request.user
            post.save()
            return JsonResponse({"response": True})
    return JsonResponse({"response": False})

def delete_note(request):
    date = request.POST.get('date')
    try:
       query = Agenda.objects.get(date=date,user=request.user).delete()
       return JsonResponse({'response': True})
    except:
        return JsonResponse({'response': False})

def get_notes(request):
    """Get All User Notes / Pegar todas as anotacoes do usuario"""
    user = request.user
    date = request.GET.get('date')
    try:
        query = Agenda.objects.get(date=date,user=user)
    except:
        query = ""
    notes = {"notes": str(query)}
    return JsonResponse(notes)