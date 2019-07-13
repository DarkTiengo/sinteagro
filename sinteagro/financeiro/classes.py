from ofxparse import OfxParser

from .models import Conta,Extrato,Saldo_Inicial

def class_extrato(request):
    if request.is_ajax:
        conta = request.GET.get('conta')
        month = request.GET.get('mes')
        try:
            cc = Conta.objects.get(id=conta,user=request.user)
            try:
                ex = Extrato.objects.filter(id=conta, date__month=month).values()
                result = list()
                for e in ex:
                    result.append(e)
                return result
            except:
                pass
        except:
            raise ValueError("Problemas de autenticacao de conta")

def class_accounts(request,banco):
    if request.is_ajax:
        ccs = Conta.objects.filter(banco=banco,user=request.user).values_list("agencia","conta")
        return ccs

def class_user_bank(request):
    cc = Conta.objects.filter(user=request.user).values_list("banco",flat=True).distinct()
    return cc

def saldo(request, ano = None, mes = None):
    if request.method == "POST":
        conta = Conta.objects.get(user=request.user,conta=request.POST['conta'])
        valor = request.POST['saldo']
        try:
            saldo_inicial = Saldo_Inicial.objects.get(user=request.user,ano=ano,mes=mes,conta=conta,saldo=valor)
            saldo_inicial.saldo = request.POST['saldo']
        except:
            saldo_inicial = Saldo_Inicial(user=request.user,ano=ano,mes=mes,saldo=valor,conta=conta)
        saldo_inicial.save()
    else:
        try:
            saldo_inicial = Saldo_Inicial.objects.get(ano=ano,mes=mes)
        except:
            saldo_inicial = None
    return saldo_inicial


class Extrato_Reader:
    conta, agencia, banco, balanco, relatorio, extrato, user = "", "", "", "",{},{},{}

    def __init__(self,file,user):
        self.user = user
        operacao, history, date, type, valor, documento = [], [], [], [], [], []
        try:
            datas = file.read()
            fileobj = open(user.email + ".ofx", "wb")
            fileobj.write(datas)
            fileobj.close()
            fileobj = open(user.email + ".ofx", "rb")
            ofx = OfxParser.parse(fileobj)
            conta = ofx.account
            self.conta = conta.account_id
            self.agencia = conta.branch_id
            self.banco = conta.institution.organization
            relatorio = conta.statement
            self.balanco = relatorio.balance
            self.relatorio.update(inicio=relatorio.start_date, fim=relatorio.end_date),
            for extrato in relatorio.transactions:
                operacao.append(extrato.id)
                valor.append(extrato.amount)
                history.append(extrato.memo)
                date.append(extrato.date)
                type.append(extrato.type)
                documento.append(extrato.checknum)
            self.extrato.update(operacao=operacao, history=history, date=date, type=type, valor=valor, documento = documento)
            fileobj.close()
        except:
            return False

    def save_extrato(self):
        pass

    def account_exist(self):
        try:
            conta = Conta.objects.get(conta=self.conta, agencia=self.agencia, user=self.user)
            return True
        except:
            return False


    def account_auto_create(self):
        if self.account_exist():
            dados = {"message": "Conta já criada","type": "alert-error"}
        else:
            conta = Conta.objects.create(user=self.user,conta=self.conta,agencia=self.agencia,banco=self.banco)
            conta.save()
            dados = {"message": "Conta criada com sucesso.","type": "alert-success","banco": self.banco}
        return dados