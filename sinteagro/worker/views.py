from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import *

@login_required
def worker(request):
    try:
        w = Worker.objects.filter(user=request.user)
        return render(request,"worker/workergeral.html",{"workers": w})
    except:
        return render(request,"worker/workergeral.html")

def worker_sign(request):
    if request.is_ajax() and request.POST:
        w = WorkerForm(request.POST)
        if w.is_valid():
            w.user = request.user
            w.save()
            return(JsonResponse({'type': 'alert-success','message': 'Funcionário cadastrado com sucesso!'}))
        else:
           return (JsonResponse({'type': 'alert-danger', 'message': 'Algo deu errado, por favor tente novamente.','dados': w.errors}))
    else:
        return render(request,"worker/cad_worker.html", {'form': WorkerForm()})
