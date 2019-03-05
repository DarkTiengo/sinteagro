from .models import Fazenda, Safra

mes = {
    1 : 'Janeiro',
    2 : 'Fevereiro'
}

ano = []
for x in range(2009, 2020):
    ano.append(x)

#Auxiliar do Views de Fazenda
def gera_Menu(usuario):
    """Gera os Dados do Menu Lateral / Main menu"""
    try:
        menu = Fazenda.objects.filter(user=usuario).order_by('data')
        contexto = {'fazendas': menu}
        return contexto
    except:
        return False

def get_fazenda_e_talhoes(fazenda_id,usuario):
    """Pega as fazendas basicas e talhoes / Get Farms and Fields"""
    try:
        fazendas = gera_Menu(usuario=usuario)
        faz = fazendas['fazendas'].get(id=fazenda_id)
        talhoes = faz.talhao_set.order_by('nome')
        tamanho = 0
        for t in talhoes:
            tamanho += int(t.tamanho)
        dados = {'talhoes': talhoes,'fazenda': faz,'tamanho': tamanho}
        dados.update(fazendas)
        return dados
    except:
        return False


def get_fazenda(fazenda_id):
    """Pegar dados da fazenda / Get a Farm"""
    dados = Fazenda.objects.get(id=fazenda_id)
    return {'fazenda': dados}

def excluir_fazenda(fazenda_id):
    """" Excluir Fazenda / Remove Farm """
    return Fazenda.objects.filter(id=fazenda_id).delete()

def get_safras(usuario):
    """Pegar todas as safras / Get All Crops"""
    safras = Safra.objects.filter(user=usuario).order_by('ano1')
    return {'safras': safras}

def safra_remove(id):
    """ Remove uma safra / Remove a Crop"""
    return Safra.objects.get(id=id).delete()
