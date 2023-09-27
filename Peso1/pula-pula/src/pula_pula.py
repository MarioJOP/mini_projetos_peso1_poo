from src.crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.filaEspera = []
        self.criancasPulando = []
        self.caixa = 0
        self.contas = {}

    def getFilaDeEspera(self):
        return self.filaEspera
    def getCriancasPulando(self):
        return self.criancasPulando

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for k, v in self.contas.items():
            if k == nome:
                return v
        print('Conta não encontrada')
        return False


    def entrarNaFila(self, crianca: Crianca):
        if crianca.getNome() in self.filaEspera:
            print('Não é possível inserir duas ou mais crianças com o mesmo nome na fila de espera')
            return False
        else:
            self.filaEspera.append(crianca.getNome())
            self.contas[crianca.getNome()] = 5.00
            return True



    def entrar(self):
        if len(self.filaEspera) > 0:
            if len(self.criancasPulando) < self.limiteMax:
                self.criancasPulando.append(self.filaEspera[0])
                del self.filaEspera[0]
                return True
            print('O pula pula está com a quantidade maxima de crianças! ')
            return False
        else:
            print('Niguem na fila')
            return False

    def sair(self):
        self.filaEspera.append(self.criancasPulando[0])
        self.criancasPulando.pop(0)
        return True

    def papaiChegou(self, nome):
        if nome in self.filaEspera:
            for k, v in self.contas.items():
                if k == nome:
                    self.caixa += v
            self.filaEspera.remove(nome)
            return True
        elif nome in self.criancasPulando:
            for k, v in self.contas.items():
                if k == nome:
                    self.caixa += v
            self.criancasPulando.remove(nome)
            return True
        else:
            print('Criança não encontrada')
            return False

    def fechar(self):
        for k, v in self.contas.items():
            self.caixa += v
        self.contas.clear()
        self.criancasPulando.clear()
        self.filaEspera.clear()
        return True
