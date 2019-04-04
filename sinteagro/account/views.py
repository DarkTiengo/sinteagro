from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm

from .models import User
from .forms import UserForm
from .auxiliar import *
from localidades.models import Cidade

def login(request):
    """Pagina Inicial de Login / System Login"""
    contexto = {"home": True}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    else:
        if request.method == "POST":
            usuario = authenticate(username=request.POST['username'], password=request.POST['password'])
            if usuario is not None:
                if usuario.is_active:
                    pass
                    if usuario.is_trusty:
                        contexto['home'] = True
                        django_login(request,usuario)
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        contexto['info'] = "Favor confirme o e-mail que foi enviado para voce."
                else:
                    contexto['info'] = "Usuario nao ativo, favor entrar em contato com o suporte."
            else:
                contexto['info'] = "Login ou Senha incorretos. Por favor tente novamente."
        return render(request,'account/login.html',contexto)

def cadastro(request):
    """"Pagina do cadastro de usuarios / User registration"""
    contexto = {"aba" : "cadastro"}
    if request.method == "POST":
        if "confirmaregistro" in request.POST:
            dados = UserForm(request.POST)
            if not dados.is_valid():
                contexto["info"] = "erro"
                contexto["mensagem"] = dados.errors
            elif not dados.check_password():
                contexto["info"] = "erro"
                contexto["mensagem"] = "A senha deve conter  entre 6 a 8 caracteres."
            else:
                dados.save()
                return render(request, "account/sucesso.html")
        else:
            contexto["info"] = "erro"
            contexto["mensagem"] = "Voce deve aceitar os termos de uso."
    return render(request,"account/cadastro.html",contexto)

def check_email(request):
    """"Check if email exist / Checa se email existe"""
    email = request.GET.get('email')
    data = {'is_taken': User.objects.filter(email__exact=email).exists() }
    return JsonResponse(data)

def get_cidade(request):
    """"Pega as cidades pelos estados / Get cities by brazilian states"""
    estado = request.GET.get('estado')
    data = Cidade.objects.filter(uf=estado).values()
    return JsonResponse({"cities": list(data)})

@login_required()
def configuracoes(request):
    """Exibe e altera informacoes do usuario / Show and edit User Information"""
    if request.method == "GET":
        cities = get_cities(request.user.estado)
        name_user_city = get_city(request.user.cidade)
        contexto = {
            'estados': select_estados,
            'user': request.user,
            'cidades': cities.values_list('id','nome'),
            'user_city': name_user_city,
        }
        return render(request,'account/configuracoes.html',contexto)
    elif request.method == "POST" and request.is_ajax:
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            response = {"type": "alert-success","message": "Alterações feitas com sucesso."}
            return JsonResponse(response)
        else:
            response = {"type": "alert-danger","message": form.errors}
            return JsonResponse(response)

@login_required()
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            response = {"type": "alert-success", "message": "Senha alterada com sucesso."}
            return JsonResponse(response)
        else:
            response = {"type": "alert-danger", "message": form.errors}
            return JsonResponse(response)
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'account/change_password.html',{'form': form})
