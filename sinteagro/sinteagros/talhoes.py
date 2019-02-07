from .models import Talhao, Produtividade

#Auxiliar dos Views dos talhoes

produtos = ("Soja","Milho")

def get_talhao(talhao_id):
    """Mostra os dados do talhao"""
    try:
        data_talhao = Talhao.objects.get(id=talhao_id)
        talhao = {'talhao': data_talhao}
    except:
        talhao = {'talhao': None}
    return talhao

def remove_talhao(talhao_id):
    """Remove o talhao"""
    try:
        Talhao.objects.get(id=talhao_id).delete()
        return True
    except:
        return False

def get_produtividade(talhao):
    """"Pega os dados da produtividade"""
    try:
        p = Produtividade.objects.get(talhao=talhao)
        return p
    except:
        return None