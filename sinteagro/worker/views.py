from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import WorkerForm, Worker

@login_required
def worker(request):
    w = Worker.objects.filter(user=request.user)
    return render(request,"worker/workergeral.html",{'workers': w})

def worker_sign(request):
    if request.is_ajax() and request.POST:
        w = WorkerForm(request.POST)
        if w.is_valid():
            #post.save()
           return(JsonResponse({'type': 'alert-success','message': 'Funcionário cadastrado com sucesso!','dados': request.POST}))
        else:
           return (JsonResponse({'type': 'alert-danger', 'message': 'Algo deu errado, por favor tente novamente.','dados': w.errors}))
    else:
        return render(request,"worker/cad_worker.html",{'user': request.user})
