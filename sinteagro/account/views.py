from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

from .models import User
from .forms import UserForm
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