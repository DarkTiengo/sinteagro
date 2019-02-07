from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from .forms import UserForm

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
