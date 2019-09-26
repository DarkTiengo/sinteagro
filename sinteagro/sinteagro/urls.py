"""sinteagro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from account.views import configuracoes,change_password
from financeiro.views import *
from worker.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',include("account.urls")),
    path('login/',include("account.urls")),
    path('index/',include('sinteagros.urls')),
    path('',include("account.urls")),
    path('configuracoes/', configuracoes,name="configuracoes"),
    path('change_password/',change_password,name="change_password"),
    path('conta/',conta,name="conta"),
    path('bancos/',get_bancos_user,name='bancos'),
    path('contas/',get_accounts,name='contas'),
    path('extrato/',get_extrato,name='extrato'),
    path('lancamento/',lancamento,name='lancamento'),
    path('set_extrato/',set_extrato,name="set_extrato"),
    path('set_auto_conta',set_auto_conta,name='set_auto_conta'),
    path('saldo/',saldo,name='saldo'),
    path('index/pggeral/',pagar_receber,name='pggeral'),
    path('data_extrato/',data_extrato,name='data_extrato'),
    path('set_contas/',set_contas,name='set_contas'),
    path('worker/',worker,name='worker'),
    path('worker_sign/',worker_sign,name='worker_sign'),
]
