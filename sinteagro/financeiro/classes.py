from ofxparse import OfxParser

from .models import Conta,Extrato,Saldo_Inicial

def class_extrato(request):
    if request.is_ajax:
        conta = request.GET.get('conta')
        month = request.GET.get('mes')
        cc = Conta.objects.get(conta=conta,user=request.user)
        ex = Extrato.objects.filter(conta=cc).values()
        return ex

def class_accounts(request,banco):
    if request.is_ajax:
        ccs = Conta.objects.filter(banco=banco,user=request.user).values_list("agencia","conta")
        return ccs

def class_user_bank(request):
    cc = Conta.objects.filter(user=request.user).values_list("banco",flat=True).distinct()
    return cc

def get_saldo(request,ano = None, mes = None):
    try:
        saldo_inicial = round(Saldo_Inicial.objects.get(ano=ano,mes=mes).saldo,2)
    except:
        saldo_inicial = None
    return saldo_inicial

def set_saldo(request):
    conta = Conta.objects.get(user=request.user, conta=request.POST['conta'])
    valor = request.POST['saldo']
    try:
        saldo_inicial = Saldo_Inicial.objects.get(user=request.user, ano=request.POST['ano'], mes=request.POST['mes'],
                                                  conta=conta)
        saldo_inicial.saldo = valor
        saldo_inicial.save()
    except Saldo_Inicial.DoesNotExist:
        saldo_inicial = Saldo_Inicial(user=request.user, ano=request.POST['ano'], mes=request.POST['mes'], saldo=valor,
                                      conta=conta)
        saldo_inicial.save()
    except:
        return False
    return True


class Extrato_Reader:
    conta_extrato, agencia, banco, balanco, relatorio, user = "", "", "", "",{},{}
    operacao, history, date, type, valor, documento = [], [], [], [], [], []
    error_control = True

    def __init__(self,file,user,conta_user):
        self.user = user
        try:
            datas = file.read()
            fileobj = open(user.email + ".ofx", "wb")
            fileobj.write(datas)
            fileobj.close()
            fileobj = open(user.email + ".ofx", "rb")
            ofx = OfxParser.parse(fileobj)
            conta = ofx.account
            self.conta_extrato = conta.account_id
            if conta_user == self.conta_extrato:
                self.error_control = True
                self.agencia = conta.branch_id
                self.banco = conta.institution.organization
                relatorio = conta.statement
                self.balanco = relatorio.balance
                self.relatorio.update(inicio=relatorio.start_date, fim=relatorio.end_date),
                for extrato in relatorio.transactions:
                    self.operacao.append(extrato.id)
                    self.valor.append(extrato.amount)
                    self.history.append(extrato.memo)
                    self.date.append(extrato.date)
                    self.type.append(extrato.type)
                    self.documento.append(extrato.checknum)
            else:
                self.error_control = False
            fileobj.close()
        except:
            self.error_control = False

    def is_valid(self):
        return self.error_control

    def save_extrato(self):
        conta = Conta.objects.get(conta=self.conta_extrato,user=self.user)
        resultado = Extrato.objects.filter(date__range=[self.relatorio["inicio"],self.relatorio["fim"]],conta=conta)
        if len(resultado) > 0:
            pass
        else:
            for x in range(len(self.operacao)):
                e = Extrato(conta=conta,operacao=self.operacao[x],history=self.history[x],type=self.type[x],document=self.documento[x],valor=self.valor[x],date=self.date[x])
                e.save()

    def account_exist(self):
        try:
            Conta.objects.get(conta=self.conta_extrato, agencia=self.agencia, user=self.user)
            return True
        except:
            return False


    def account_auto_create(self):
        if self.account_exist():
            dados = {"message": "Conta já criada","type": "alert-error"}
        else:
            conta = Conta.objects.create(user=self.user,conta=self.conta_extrato,agencia=self.agencia,banco=self.banco)
            conta.save()
            dados = {"message": "Conta criada com sucesso.","type": "alert-success","banco": self.banco}
        return dados