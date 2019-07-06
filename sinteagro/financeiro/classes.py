from ofxparse import OfxParser

from .models import Conta,Extrato

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

class Extrato_Reader:
    conta, agencia, banco, balanco, relatorio, extrato, user = "", "", "", "",{},{},{}

    def __init__(self,file,user):
        self.user = user
        id, content, date, type, amount = [], [], [], [], []
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
                id.append(extrato.id)
                amount.append(extrato.amount)
                content.append(extrato.memo)
                date.append(extrato.date)
                type.append(extrato.type)
            self.extrato.update(operacao=id, history=content, date=date, type=type, valor=amount)
            fileobj.close()
        except:
            return False

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