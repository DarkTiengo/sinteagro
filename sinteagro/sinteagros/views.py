from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime

from .forms import AgendaForm
from .models import Agenda
from financeiro.views import extrato

@login_required()
def index(request):
    """Pagina inicial  / Main Menu"""
    return render(request,'sinteagros/index.html',extrato(request))

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